"""Generated from Smithy shape ``com.amazonaws.dynamodb#Select``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_dynamodb.errors import DeserializationError

Select: TypeAlias = Literal[
    "ALL_ATTRIBUTES",
    "ALL_PROJECTED_ATTRIBUTES",
    "SPECIFIC_ATTRIBUTES",
    "COUNT",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL_ATTRIBUTES",
        "ALL_PROJECTED_ATTRIBUTES",
        "SPECIFIC_ATTRIBUTES",
        "COUNT",
    )
)


def serialize_aws_json_1_0(value: Select) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Select:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Select value: {data!r}")
    return cast(Select, data)
