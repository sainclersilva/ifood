# This is an example feature definition file

from datetime import timedelta

import pandas as pd
import importlib

from feast import (
    Entity,
    FeatureService,
    FeatureView,
    Field,
    FileSource,
    PushSource,
    RequestSource
)
from feast.feature_logging import LoggingConfig
from feast.infra.offline_stores.file_source import FileLoggingDestination
from feast.on_demand_feature_view import on_demand_feature_view
from feast.types import Float32, Float64, Int64, Bool, String
from pathlib import Path

# Definir a raiz do projeto
BASE_DIR = Path("ifood").resolve().parent
print(f'Diretorio encontrado: {BASE_DIR}')

restaurant_entity = Entity(name = "restaurant_id", join_keys=["id"])

#Predictor feature view
restaurant_source = FileSource(
    name="restaurant_fs",
    path=f"{BASE_DIR}/data/restaurant.parquet",
    event_timestamp_column="timestamp_col",
)

restaurant_fv = FeatureView(
    name="restaurant_fview",
    ttl = timedelta(seconds=3600),
    entities=[restaurant_entity],
    schema=[
        Field(name="enabled", dtype=Bool, description="Restaurant status"),
        Field(name="price_range", dtype=Int64, description="Price"),
        Field(name="average_ticket", dtype=Float64, description="AvTicket"),
        Field(name="takeout_time", dtype=Int64, description="Takeout"),
        Field(name="delivery_time", dtype=Float64, description="Delivery TIme"),
        Field(name="minimum_order_value", dtype=Float64, description="Order Value"),
        Field(name="merchant_zip_code", dtype=Int64, description="ZipCode"),
        Field(name="merchant_city", dtype=String, description="Takeout"),
        Field(name="merchant_state", dtype=String, description="State"),
        Field(name="merchant_country", dtype=String, description="Country"),
    ],
    source=restaurant_source,
    online = True,
    tags={},
)