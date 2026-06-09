"""Generated from Smithy shape ``com.amazonaws.kms#MessageType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_kms.errors import DeserializationError

MessageType: TypeAlias = Literal[
    "RAW",
    "DIGEST",
    "EXTERNAL_MU",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RAW",
        "DIGEST",
        "EXTERNAL_MU",
    )
)


def serialize_aws_json_1_1(value: MessageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MessageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MessageType value: {data!r}")
    return cast(MessageType, data)
