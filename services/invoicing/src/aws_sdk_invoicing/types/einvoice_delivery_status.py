"""Generated from Smithy shape ``com.amazonaws.invoicing#EinvoiceDeliveryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_invoicing.errors import DeserializationError

EinvoiceDeliveryStatus: TypeAlias = Literal[
    "DELIVERED",
    "NOT_DELIVERED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DELIVERED",
        "NOT_DELIVERED",
    )
)


def serialize_aws_json_1_0(value: EinvoiceDeliveryStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EinvoiceDeliveryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EinvoiceDeliveryStatus value: {data!r}")
    return cast(EinvoiceDeliveryStatus, data)
