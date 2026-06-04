"""Generated from Smithy shape ``com.amazonaws.ecs#ClusterField``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

ClusterField: TypeAlias = Literal[
    "ATTACHMENTS",
    "CONFIGURATIONS",
    "SETTINGS",
    "STATISTICS",
    "TAGS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ATTACHMENTS",
        "CONFIGURATIONS",
        "SETTINGS",
        "STATISTICS",
        "TAGS",
    )
)


def serialize_aws_json_1_1(value: ClusterField) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterField value: {data!r}")
    return cast(ClusterField, data)
