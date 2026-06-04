"""Generated from Smithy shape ``com.amazonaws.dynamodb#AttributeAction``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_dynamodb.errors import DeserializationError

AttributeAction: TypeAlias = Literal[
    "ADD",
    "PUT",
    "DELETE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ADD",
        "PUT",
        "DELETE",
    )
)


def serialize_aws_json_1_0(value: AttributeAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AttributeAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttributeAction value: {data!r}")
    return cast(AttributeAction, data)
