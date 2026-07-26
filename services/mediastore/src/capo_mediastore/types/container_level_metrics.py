"""Generated from Smithy shape ``com.amazonaws.mediastore#ContainerLevelMetrics``."""

from typing import Literal, TypeAlias, cast

ContainerLevelMetrics: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerLevelMetrics) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerLevelMetrics:
    return cast(ContainerLevelMetrics, data)
