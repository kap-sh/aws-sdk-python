"""Generated from Smithy shape ``com.amazonaws.taxsettings#ChileAdditionalInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.chile_document_type
    import aws_sdk_taxsettings.types.generic_string

class ChileAdditionalInfo(TypedDict):
    document_type: NotRequired["aws_sdk_taxsettings.types.chile_document_type.ChileDocumentType"]
    """<p> The type of tax document. For Chile, this can be <code>Invoice</code> or <code>Receipt</code>.</p>"""
    business_activity: NotRequired["aws_sdk_taxsettings.types.generic_string.GenericString"]
    """<p> The business activity of the taxpayer in Chile.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ChileAdditionalInfo) -> dict:
    out: dict = {}
    if "document_type" in value:
        import aws_sdk_taxsettings.types.chile_document_type
        out["documentType"] = aws_sdk_taxsettings.types.chile_document_type.serialize_json(value["document_type"])
    if "business_activity" in value:
        out["businessActivity"] = value["business_activity"]
    return out


def deserialize_json(data: dict) -> ChileAdditionalInfo:
    out: ChileAdditionalInfo = {}  # type: ignore[typeddict-item]
    if "documentType" in data:
        import aws_sdk_taxsettings.types.chile_document_type
        out["document_type"] = aws_sdk_taxsettings.types.chile_document_type.deserialize_json(data["documentType"])
    if "businessActivity" in data:
        out["business_activity"] = data["businessActivity"]
    return out