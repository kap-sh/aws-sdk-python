"""Generated from Smithy shape ``com.amazonaws.invoicing#InvoicePDF``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_invoicing.types.string_without_new_line
    import capo_invoicing.types.supplemental_documents


class InvoicePDF(TypedDict, closed=True):
    invoice_id: NotRequired[
        "capo_invoicing.types.string_without_new_line.StringWithoutNewLine"
    ]
    """<p> Your unique invoice ID. </p>"""
    document_url: NotRequired[
        "capo_invoicing.types.string_without_new_line.StringWithoutNewLine"
    ]
    """<p>The pre-signed URL to download the invoice document. </p>"""
    document_url_expiration_date: NotRequired["datetime.datetime"]
    """<p>The pre-signed URL expiration date of the invoice document.</p>"""
    supplemental_documents: NotRequired[
        "capo_invoicing.types.supplemental_documents.SupplementalDocuments"
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
        import capo_invoicing.types._prelude.timestamp

        out["DocumentUrlExpirationDate"] = (
            capo_invoicing.types._prelude.timestamp.serialize_aws_json_1_0(
                value["document_url_expiration_date"]
            )
        )
    if "supplemental_documents" in value:
        import capo_invoicing.types.supplemental_documents

        out["SupplementalDocuments"] = (
            capo_invoicing.types.supplemental_documents.serialize_aws_json_1_0(
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
        import capo_invoicing.types._prelude.timestamp

        out["document_url_expiration_date"] = (
            capo_invoicing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["DocumentUrlExpirationDate"]
            )
        )
    if "SupplementalDocuments" in data:
        import capo_invoicing.types.supplemental_documents

        out["supplemental_documents"] = (
            capo_invoicing.types.supplemental_documents.deserialize_aws_json_1_0(
                data["SupplementalDocuments"]
            )
        )
    return out
