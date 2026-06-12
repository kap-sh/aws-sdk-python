"""Generated from Smithy shape ``com.amazonaws.mediastore#ContainerLevelMetrics``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediastore.errors import DeserializationError

ContainerLevelMetrics: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: ContainerLevelMetrics) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerLevelMetrics:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContainerLevelMetrics value: {data!r}")
    return cast(ContainerLevelMetrics, data)
