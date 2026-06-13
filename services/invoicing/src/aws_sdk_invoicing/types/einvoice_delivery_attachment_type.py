"""Generated from Smithy shape ``com.amazonaws.invoicing#EinvoiceDeliveryAttachmentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_invoicing.errors import DeserializationError

EinvoiceDeliveryAttachmentType: TypeAlias = Literal[
    "INVOICE_PDF",
    "RFP_PDF",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INVOICE_PDF",
        "RFP_PDF",
    )
)


def serialize_aws_json_1_0(value: EinvoiceDeliveryAttachmentType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EinvoiceDeliveryAttachmentType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EinvoiceDeliveryAttachmentType value: {data!r}"
        )
    return cast(EinvoiceDeliveryAttachmentType, data)
