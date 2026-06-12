"""Generated from Smithy shape ``com.amazonaws.devicefarm#OfferingTransactionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_device_farm.errors import DeserializationError

OfferingTransactionType: TypeAlias = Literal[
    "PURCHASE",
    "RENEW",
    "SYSTEM",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PURCHASE",
        "RENEW",
        "SYSTEM",
    )
)


def serialize_aws_json_1_1(value: OfferingTransactionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OfferingTransactionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OfferingTransactionType value: {data!r}")
    return cast(OfferingTransactionType, data)
