"""Generated from Smithy shape ``com.amazonaws.invoicing#EinvoiceDeliveryAttachmentTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_invoicing.types.einvoice_delivery_attachment_type

EinvoiceDeliveryAttachmentTypes: TypeAlias = list[
    "capo_invoicing.types.einvoice_delivery_attachment_type.EinvoiceDeliveryAttachmentType"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EinvoiceDeliveryAttachmentTypes) -> list:
    import capo_invoicing.types.einvoice_delivery_attachment_type

    out: list = []
    for item in value:
        out.append(
            capo_invoicing.types.einvoice_delivery_attachment_type.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EinvoiceDeliveryAttachmentTypes:
    import capo_invoicing.types.einvoice_delivery_attachment_type

    out: EinvoiceDeliveryAttachmentTypes = []
    for item in data:
        out.append(
            capo_invoicing.types.einvoice_delivery_attachment_type.deserialize_aws_json_1_0(
                item
            )
        )
    return out
