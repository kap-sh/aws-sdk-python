"""Generated from Smithy shape ``com.amazonaws.appsync#ResolverLevelMetricsConfig``."""

from typing import Literal, TypeAlias, cast

ResolverLevelMetricsConfig: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResolverLevelMetricsConfig) -> str:
    return value


def deserialize_json(data: str) -> ResolverLevelMetricsConfig:
    return cast(ResolverLevelMetricsConfig, data)
