"""Generated from Smithy shape ``com.amazonaws.invoicing#EinvoiceDeliveryPreference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_invoicing.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_invoicing.types.connection_testing_method
    import aws_sdk_invoicing.types.einvoice_delivery_attachment_types
    import aws_sdk_invoicing.types.einvoice_delivery_document_types
    import aws_sdk_invoicing.types.protocol
    import aws_sdk_invoicing.types.purchase_order_data_sources


class EinvoiceDeliveryPreference(TypedDict, closed=True):
    einvoice_delivery_document_types: "aws_sdk_invoicing.types.einvoice_delivery_document_types.EinvoiceDeliveryDocumentTypes"
    """<p>The types of e-invoice documents to be delivered.</p>"""
    einvoice_delivery_attachment_types: NotRequired[
        "aws_sdk_invoicing.types.einvoice_delivery_attachment_types.EinvoiceDeliveryAttachmentTypes"
    ]
    """<p>The types of attachments to include with the e-invoice delivery.</p>"""
    protocol: "aws_sdk_invoicing.types.protocol.Protocol"
    """<p>The communication protocol to use for e-invoice delivery.</p>"""
    purchase_order_data_sources: (
        "aws_sdk_invoicing.types.purchase_order_data_sources.PurchaseOrderDataSources"
    )
    """<p>The sources of purchase order data to use for e-invoice generation and delivery.</p>"""
    connection_testing_method: (
        "aws_sdk_invoicing.types.connection_testing_method.ConnectionTestingMethod"
    )
    """<p>The method to use for testing the connection to the procurement portal.</p>"""
    einvoice_delivery_activation_date: "datetime.datetime"
    """<p>The date when e-invoice delivery should be activated for this preference.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EinvoiceDeliveryPreference) -> dict:
    out: dict = {}
    import aws_sdk_invoicing.types.einvoice_delivery_document_types

    out["EinvoiceDeliveryDocumentTypes"] = (
        aws_sdk_invoicing.types.einvoice_delivery_document_types.serialize_aws_json_1_0(
            value["einvoice_delivery_document_types"]
        )
    )
    if "einvoice_delivery_attachment_types" in value:
        import aws_sdk_invoicing.types.einvoice_delivery_attachment_types

        out["EinvoiceDeliveryAttachmentTypes"] = (
            aws_sdk_invoicing.types.einvoice_delivery_attachment_types.serialize_aws_json_1_0(
                value["einvoice_delivery_attachment_types"]
            )
        )
    import aws_sdk_invoicing.types.protocol

    out["Protocol"] = aws_sdk_invoicing.types.protocol.serialize_aws_json_1_0(
        value["protocol"]
    )
    import aws_sdk_invoicing.types.purchase_order_data_sources

    out["PurchaseOrderDataSources"] = (
        aws_sdk_invoicing.types.purchase_order_data_sources.serialize_aws_json_1_0(
            value["purchase_order_data_sources"]
        )
    )
    import aws_sdk_invoicing.types.connection_testing_method

    out["ConnectionTestingMethod"] = (
        aws_sdk_invoicing.types.connection_testing_method.serialize_aws_json_1_0(
            value["connection_testing_method"]
        )
    )
    import aws_sdk_invoicing.types._prelude.timestamp

    out["EinvoiceDeliveryActivationDate"] = (
        aws_sdk_invoicing.types._prelude.timestamp.serialize_aws_json_1_0(
            value["einvoice_delivery_activation_date"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> EinvoiceDeliveryPreference:
    out: EinvoiceDeliveryPreference = {}  # type: ignore[typeddict-item]
    if "EinvoiceDeliveryDocumentTypes" in data:
        import aws_sdk_invoicing.types.einvoice_delivery_document_types

        out["einvoice_delivery_document_types"] = (
            aws_sdk_invoicing.types.einvoice_delivery_document_types.deserialize_aws_json_1_0(
                data["EinvoiceDeliveryDocumentTypes"]
            )
        )
    else:
        raise DeserializationError(
            "EinvoiceDeliveryPreference.einvoice_delivery_document_types required"
        )
    if "EinvoiceDeliveryAttachmentTypes" in data:
        import aws_sdk_invoicing.types.einvoice_delivery_attachment_types

        out["einvoice_delivery_attachment_types"] = (
            aws_sdk_invoicing.types.einvoice_delivery_attachment_types.deserialize_aws_json_1_0(
                data["EinvoiceDeliveryAttachmentTypes"]
            )
        )
    if "Protocol" in data:
        import aws_sdk_invoicing.types.protocol

        out["protocol"] = aws_sdk_invoicing.types.protocol.deserialize_aws_json_1_0(
            data["Protocol"]
        )
    else:
        raise DeserializationError("EinvoiceDeliveryPreference.protocol required")
    if "PurchaseOrderDataSources" in data:
        import aws_sdk_invoicing.types.purchase_order_data_sources

        out["purchase_order_data_sources"] = (
            aws_sdk_invoicing.types.purchase_order_data_sources.deserialize_aws_json_1_0(
                data["PurchaseOrderDataSources"]
            )
        )
    else:
        raise DeserializationError(
            "EinvoiceDeliveryPreference.purchase_order_data_sources required"
        )
    if "ConnectionTestingMethod" in data:
        import aws_sdk_invoicing.types.connection_testing_method

        out["connection_testing_method"] = (
            aws_sdk_invoicing.types.connection_testing_method.deserialize_aws_json_1_0(
                data["ConnectionTestingMethod"]
            )
        )
    else:
        raise DeserializationError(
            "EinvoiceDeliveryPreference.connection_testing_method required"
        )
    if "EinvoiceDeliveryActivationDate" in data:
        import aws_sdk_invoicing.types._prelude.timestamp

        out["einvoice_delivery_activation_date"] = (
            aws_sdk_invoicing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["EinvoiceDeliveryActivationDate"]
            )
        )
    else:
        raise DeserializationError(
            "EinvoiceDeliveryPreference.einvoice_delivery_activation_date required"
        )
    return out
