"""Generated from Smithy shape ``com.amazonaws.invoicing#EinvoiceDeliveryAttachmentType``."""

from typing import Literal, TypeAlias, cast

EinvoiceDeliveryAttachmentType: TypeAlias = Literal[
    "INVOICE_PDF",
    "RFP_PDF",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EinvoiceDeliveryAttachmentType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EinvoiceDeliveryAttachmentType:
    return cast(EinvoiceDeliveryAttachmentType, data)
