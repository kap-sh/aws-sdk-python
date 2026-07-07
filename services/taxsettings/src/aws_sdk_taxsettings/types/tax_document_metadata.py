"""Generated from Smithy shape ``com.amazonaws.taxsettings#TaxDocumentMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.tax_document_access_token
    import aws_sdk_taxsettings.types.tax_document_name


class TaxDocumentMetadata(TypedDict, closed=True):
    tax_document_access_token: (
        "aws_sdk_taxsettings.types.tax_document_access_token.TaxDocumentAccessToken"
    )
    """<p>The tax document access token, which contains information that the Tax Settings API uses to locate the tax document.</p> <note> <p>If you update your tax registration, the existing <code>taxDocumentAccessToken</code> won't be valid. To get the latest token, call the <code>GetTaxRegistration</code> or <code>ListTaxRegistrations</code> API operation. This token is valid for 24 hours.</p> </note>"""
    tax_document_name: "aws_sdk_taxsettings.types.tax_document_name.TaxDocumentName"
    """<p>The name of your tax document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaxDocumentMetadata) -> dict:
    out: dict = {}
    out["taxDocumentAccessToken"] = value["tax_document_access_token"]
    out["taxDocumentName"] = value["tax_document_name"]
    return out


def deserialize_json(data: dict) -> TaxDocumentMetadata:
    out: TaxDocumentMetadata = {}  # type: ignore[typeddict-item]
    if "taxDocumentAccessToken" in data:
        out["tax_document_access_token"] = data["taxDocumentAccessToken"]
    else:
        raise DeserializationError(
            "TaxDocumentMetadata.tax_document_access_token required"
        )
    if "taxDocumentName" in data:
        out["tax_document_name"] = data["taxDocumentName"]
    else:
        raise DeserializationError("TaxDocumentMetadata.tax_document_name required")
    return out
