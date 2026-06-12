"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#KeyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

KeyType: TypeAlias = Literal[
    "AWS_OWNED_KEY",
    "CUSTOMER_MANAGED_KEY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_OWNED_KEY",
        "CUSTOMER_MANAGED_KEY",
    )
)


def serialize_aws_json_1_1(value: KeyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KeyType value: {data!r}")
    return cast(KeyType, data)
