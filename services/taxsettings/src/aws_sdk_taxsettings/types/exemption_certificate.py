"""Generated from Smithy shape ``com.amazonaws.taxsettings#ExemptionCertificate``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_taxsettings.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.exemption_document_name
    import aws_sdk_taxsettings.types.exemption_file_blob

class ExemptionCertificate(TypedDict):
    document_name: "aws_sdk_taxsettings.types.exemption_document_name.ExemptionDocumentName"
    """<p>The exemption certificate file name. </p>"""
    document_file: "aws_sdk_taxsettings.types.exemption_file_blob.ExemptionFileBlob"
    """<p>The exemption certificate file content. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ExemptionCertificate) -> dict:
    out: dict = {}
    out["documentName"] = value["document_name"]
    import aws_sdk_taxsettings.types.exemption_file_blob
    out["documentFile"] = aws_sdk_taxsettings.types.exemption_file_blob.serialize_json(value["document_file"])
    return out


def deserialize_json(data: dict) -> ExemptionCertificate:
    out: ExemptionCertificate = {}  # type: ignore[typeddict-item]
    if "documentName" in data:
        out["document_name"] = data["documentName"]
    else:
        raise DeserializationError("ExemptionCertificate.document_name required")
    if "documentFile" in data:
        import aws_sdk_taxsettings.types.exemption_file_blob
        out["document_file"] = aws_sdk_taxsettings.types.exemption_file_blob.deserialize_json(data["documentFile"])
    else:
        raise DeserializationError("ExemptionCertificate.document_file required")
    return out