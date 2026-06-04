"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalTableStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_dynamodb.errors import DeserializationError

GlobalTableStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "UPDATING",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "DELETING",
        "UPDATING",
    )
)


def serialize_aws_json_1_0(value: GlobalTableStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> GlobalTableStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GlobalTableStatus value: {data!r}")
    return cast(GlobalTableStatus, data)
