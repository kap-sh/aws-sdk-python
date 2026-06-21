"""Generated from Smithy shape ``com.amazonaws.appsync#DataSourceLevelMetricsConfig``."""

from typing import Literal, TypeAlias, cast

DataSourceLevelMetricsConfig: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceLevelMetricsConfig) -> str:
    return value


def deserialize_json(data: str) -> DataSourceLevelMetricsConfig:
    return cast(DataSourceLevelMetricsConfig, data)
