"""Generated from Smithy shape ``com.amazonaws.appsync#DataSourceLevelMetricsBehavior``."""

from typing import Literal, TypeAlias, cast

DataSourceLevelMetricsBehavior: TypeAlias = Literal[
    "FULL_REQUEST_DATA_SOURCE_METRICS",
    "PER_DATA_SOURCE_METRICS",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceLevelMetricsBehavior) -> str:
    return value


def deserialize_json(data: str) -> DataSourceLevelMetricsBehavior:
    return cast(DataSourceLevelMetricsBehavior, data)
