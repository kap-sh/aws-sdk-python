"""Generated from Smithy shape ``com.amazonaws.invoicing#EinvoiceDeliveryDocumentTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.einvoice_delivery_document_type

EinvoiceDeliveryDocumentTypes: TypeAlias = list[
    "aws_sdk_invoicing.types.einvoice_delivery_document_type.EinvoiceDeliveryDocumentType"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EinvoiceDeliveryDocumentTypes) -> list:
    import aws_sdk_invoicing.types.einvoice_delivery_document_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_invoicing.types.einvoice_delivery_document_type.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EinvoiceDeliveryDocumentTypes:
    import aws_sdk_invoicing.types.einvoice_delivery_document_type

    out: EinvoiceDeliveryDocumentTypes = []
    for item in data:
        out.append(
            aws_sdk_invoicing.types.einvoice_delivery_document_type.deserialize_aws_json_1_0(
                item
            )
        )
    return out
