"""Generated from Smithy shape ``com.amazonaws.appsync#ResolverLevelMetricsBehavior``."""

from typing import Literal, TypeAlias, cast

ResolverLevelMetricsBehavior: TypeAlias = Literal[
    "FULL_REQUEST_RESOLVER_METRICS",
    "PER_RESOLVER_METRICS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResolverLevelMetricsBehavior) -> str:
    return value


def deserialize_json(data: str) -> ResolverLevelMetricsBehavior:
    return cast(ResolverLevelMetricsBehavior, data)
