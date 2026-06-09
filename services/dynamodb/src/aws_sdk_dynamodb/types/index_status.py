"""Generated from Smithy shape ``com.amazonaws.dynamodb#IndexStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dynamodb.errors import DeserializationError

IndexStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "DELETING",
    "ACTIVE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "UPDATING",
        "DELETING",
        "ACTIVE",
    )
)


def serialize_aws_json_1_0(value: IndexStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IndexStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IndexStatus value: {data!r}")
    return cast(IndexStatus, data)
