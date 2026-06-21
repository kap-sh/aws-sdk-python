"""Generated from Smithy shape ``com.amazonaws.appsync#CacheHealthMetricsConfig``."""

from typing import Literal, TypeAlias, cast

CacheHealthMetricsConfig: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CacheHealthMetricsConfig) -> str:
    return value


def deserialize_json(data: str) -> CacheHealthMetricsConfig:
    return cast(CacheHealthMetricsConfig, data)
