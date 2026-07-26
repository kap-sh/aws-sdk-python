"""Generated from Smithy shape ``com.amazonaws.invoicing#SupplementalDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_invoicing.types.string_without_new_line
    import capo_invoicing.types.supplemental_document_type


class SupplementalDocument(TypedDict, closed=True):
    document_type: NotRequired[
        "capo_invoicing.types.supplemental_document_type.SupplementalDocumentType"
    ]
    """<p>The type of supplemental document.</p>"""
    document_id: NotRequired[
        "capo_invoicing.types.string_without_new_line.StringWithoutNewLine"
    ]
    """<p>The ID of the supplemental document.</p>"""
    document_url: NotRequired[
        "capo_invoicing.types.string_without_new_line.StringWithoutNewLine"
    ]
    """<p>The pre-signed URL to download invoice supplemental document.</p>"""
    document_url_expiration_date: NotRequired["datetime.datetime"]
    """<p>The pre-signed URL expiration date of invoice supplemental document.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SupplementalDocument) -> dict:
    out: dict = {}
    if "document_type" in value:
        import capo_invoicing.types.supplemental_document_type

        out["DocumentType"] = (
            capo_invoicing.types.supplemental_document_type.serialize_aws_json_1_0(
                value["document_type"]
            )
        )
    if "document_id" in value:
        out["DocumentId"] = value["document_id"]
    if "document_url" in value:
        out["DocumentUrl"] = value["document_url"]
    if "document_url_expiration_date" in value:
        import capo_invoicing.types._prelude.timestamp

        out["DocumentUrlExpirationDate"] = (
            capo_invoicing.types._prelude.timestamp.serialize_aws_json_1_0(
                value["document_url_expiration_date"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SupplementalDocument:
    out: SupplementalDocument = {}  # type: ignore[typeddict-item]
    if "DocumentType" in data:
        import capo_invoicing.types.supplemental_document_type

        out["document_type"] = (
            capo_invoicing.types.supplemental_document_type.deserialize_aws_json_1_0(
                data["DocumentType"]
            )
        )
    if "DocumentId" in data:
        out["document_id"] = data["DocumentId"]
    if "DocumentUrl" in data:
        out["document_url"] = data["DocumentUrl"]
    if "DocumentUrlExpirationDate" in data:
        import capo_invoicing.types._prelude.timestamp

        out["document_url_expiration_date"] = (
            capo_invoicing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["DocumentUrlExpirationDate"]
            )
        )
    return out
