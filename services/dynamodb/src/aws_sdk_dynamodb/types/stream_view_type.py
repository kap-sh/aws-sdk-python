"""Generated from Smithy shape ``com.amazonaws.dynamodb#StreamViewType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_dynamodb.errors import DeserializationError

StreamViewType: TypeAlias = Literal[
    "NEW_IMAGE",
    "OLD_IMAGE",
    "NEW_AND_OLD_IMAGES",
    "KEYS_ONLY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NEW_IMAGE",
        "OLD_IMAGE",
        "NEW_AND_OLD_IMAGES",
        "KEYS_ONLY",
    )
)


def serialize_aws_json_1_0(value: StreamViewType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StreamViewType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StreamViewType value: {data!r}")
    return cast(StreamViewType, data)
