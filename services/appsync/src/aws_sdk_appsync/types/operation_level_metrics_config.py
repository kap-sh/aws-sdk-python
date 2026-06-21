"""Generated from Smithy shape ``com.amazonaws.appsync#OperationLevelMetricsConfig``."""

from typing import Literal, TypeAlias, cast

OperationLevelMetricsConfig: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: OperationLevelMetricsConfig) -> str:
    return value


def deserialize_json(data: str) -> OperationLevelMetricsConfig:
    return cast(OperationLevelMetricsConfig, data)
