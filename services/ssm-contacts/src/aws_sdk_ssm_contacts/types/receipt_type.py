"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ReceiptType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_contacts.errors import DeserializationError

ReceiptType: TypeAlias = Literal[
    "DELIVERED",
    "ERROR",
    "READ",
    "SENT",
    "STOP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DELIVERED",
        "ERROR",
        "READ",
        "SENT",
        "STOP",
    )
)


def serialize_aws_json_1_1(value: ReceiptType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReceiptType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReceiptType value: {data!r}")
    return cast(ReceiptType, data)
