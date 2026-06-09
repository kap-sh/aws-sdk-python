"""Generated from Smithy shape ``com.amazonaws.kms#KeyManagerType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_kms.errors import DeserializationError

KeyManagerType: TypeAlias = Literal[
    "AWS",
    "CUSTOMER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS",
        "CUSTOMER",
    )
)


def serialize_aws_json_1_1(value: KeyManagerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyManagerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KeyManagerType value: {data!r}")
    return cast(KeyManagerType, data)
