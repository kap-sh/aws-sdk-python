"""Generated from Smithy shape ``com.amazonaws.firehose#KeyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

KeyType: TypeAlias = Literal[
    "AWS_OWNED_CMK",
    "CUSTOMER_MANAGED_CMK",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_OWNED_CMK",
        "CUSTOMER_MANAGED_CMK",
    )
)


def serialize_aws_json_1_1(value: KeyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KeyType value: {data!r}")
    return cast(KeyType, data)
