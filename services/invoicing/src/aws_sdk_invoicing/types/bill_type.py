"""Generated from Smithy shape ``com.amazonaws.invoicing#BillType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_invoicing.errors import DeserializationError

BillType: TypeAlias = Literal[
    "ANNIVERSARY",
    "PURCHASE",
    "REFUND",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ANNIVERSARY",
        "PURCHASE",
        "REFUND",
    )
)


def serialize_aws_json_1_0(value: BillType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BillType value: {data!r}")
    return cast(BillType, data)
