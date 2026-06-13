"""Generated from Smithy shape ``com.amazonaws.invoicing#InvoicePDF``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_invoicing.types.string_without_new_line
    import aws_sdk_invoicing.types.supplemental_documents


class InvoicePDF(TypedDict):
    invoice_id: NotRequired[
        "aws_sdk_invoicing.types.string_without_new_line.StringWithoutNewLine"
    ]
    """<p> Your unique invoice ID. </p>"""
    document_url: NotRequired[
        "aws_sdk_invoicing.types.string_without_new_line.StringWithoutNewLine"
    ]
    """<p>The pre-signed URL to download the invoice document. </p>"""
    document_url_expiration_date: NotRequired["datetime.datetime"]
    """<p>The pre-signed URL expiration date of the invoice document.</p>"""
    supplemental_documents: NotRequired[
        "aws_sdk_invoicing.types.supplemental_documents.SupplementalDocuments"
    ]
    """<p>List of supplemental documents associated with the invoice.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvoicePDF) -> dict:
    out: dict = {}
    if "invoice_id" in value:
        out["InvoiceId"] = value["invoice_id"]
    if "document_url" in value:
        out["DocumentUrl"] = value["document_url"]
    if "document_url_expiration_date" in value:
        import aws_sdk_invoicing.types._prelude.timestamp

        out["DocumentUrlExpirationDate"] = (
            aws_sdk_invoicing.types._prelude.timestamp.serialize_aws_json_1_0(
                value["document_url_expiration_date"]
            )
        )
    if "supplemental_documents" in value:
        import aws_sdk_invoicing.types.supplemental_documents

        out["SupplementalDocuments"] = (
            aws_sdk_invoicing.types.supplemental_documents.serialize_aws_json_1_0(
                value["supplemental_documents"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InvoicePDF:
    out: InvoicePDF = {}  # type: ignore[typeddict-item]
    if "InvoiceId" in data:
        out["invoice_id"] = data["InvoiceId"]
    if "DocumentUrl" in data:
        out["document_url"] = data["DocumentUrl"]
    if "DocumentUrlExpirationDate" in data:
        import aws_sdk_invoicing.types._prelude.timestamp

        out["document_url_expiration_date"] = (
            aws_sdk_invoicing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["DocumentUrlExpirationDate"]
            )
        )
    if "SupplementalDocuments" in data:
        import aws_sdk_invoicing.types.supplemental_documents

        out["supplemental_documents"] = (
            aws_sdk_invoicing.types.supplemental_documents.deserialize_aws_json_1_0(
                data["SupplementalDocuments"]
            )
        )
    return out
