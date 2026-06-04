"""Generated from Smithy shape ``com.amazonaws.dynamodb#ProjectionType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_dynamodb.errors import DeserializationError

ProjectionType: TypeAlias = Literal[
    "ALL",
    "KEYS_ONLY",
    "INCLUDE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "KEYS_ONLY",
        "INCLUDE",
    )
)


def serialize_aws_json_1_0(value: ProjectionType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProjectionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProjectionType value: {data!r}")
    return cast(ProjectionType, data)
