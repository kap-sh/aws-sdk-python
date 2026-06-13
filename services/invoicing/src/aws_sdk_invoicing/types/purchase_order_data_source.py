"""Generated from Smithy shape ``com.amazonaws.invoicing#PurchaseOrderDataSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.einvoice_delivery_document_type
    import aws_sdk_invoicing.types.purchase_order_data_source_type


class PurchaseOrderDataSource(TypedDict):
    einvoice_delivery_document_type: NotRequired[
        "aws_sdk_invoicing.types.einvoice_delivery_document_type.EinvoiceDeliveryDocumentType"
    ]
    """<p>The type of e-invoice document that requires purchase order data.</p>"""
    purchase_order_data_source_type: NotRequired[
        "aws_sdk_invoicing.types.purchase_order_data_source_type.PurchaseOrderDataSourceType"
    ]
    """<p>The type of source for purchase order data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PurchaseOrderDataSource) -> dict:
    out: dict = {}
    if "einvoice_delivery_document_type" in value:
        import aws_sdk_invoicing.types.einvoice_delivery_document_type

        out["EinvoiceDeliveryDocumentType"] = (
            aws_sdk_invoicing.types.einvoice_delivery_document_type.serialize_aws_json_1_0(
                value["einvoice_delivery_document_type"]
            )
        )
    if "purchase_order_data_source_type" in value:
        import aws_sdk_invoicing.types.purchase_order_data_source_type

        out["PurchaseOrderDataSourceType"] = (
            aws_sdk_invoicing.types.purchase_order_data_source_type.serialize_aws_json_1_0(
                value["purchase_order_data_source_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PurchaseOrderDataSource:
    out: PurchaseOrderDataSource = {}  # type: ignore[typeddict-item]
    if "EinvoiceDeliveryDocumentType" in data:
        import aws_sdk_invoicing.types.einvoice_delivery_document_type

        out["einvoice_delivery_document_type"] = (
            aws_sdk_invoicing.types.einvoice_delivery_document_type.deserialize_aws_json_1_0(
                data["EinvoiceDeliveryDocumentType"]
            )
        )
    if "PurchaseOrderDataSourceType" in data:
        import aws_sdk_invoicing.types.purchase_order_data_source_type

        out["purchase_order_data_source_type"] = (
            aws_sdk_invoicing.types.purchase_order_data_source_type.deserialize_aws_json_1_0(
                data["PurchaseOrderDataSourceType"]
            )
        )
    return out
