"""Generated from Smithy shape ``com.amazonaws.taxsettings#TaxRegistrationDocFile``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.file_blob
    import aws_sdk_taxsettings.types.tax_document_name


class TaxRegistrationDocFile(TypedDict):
    file_name: "aws_sdk_taxsettings.types.tax_document_name.TaxDocumentName"
    """<p>The tax registration document name. </p>"""
    file_content: "aws_sdk_taxsettings.types.file_blob.FileBlob"
    """<p>The tax registration document content. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaxRegistrationDocFile) -> dict:
    out: dict = {}
    out["fileName"] = value["file_name"]
    import aws_sdk_taxsettings.types.file_blob

    out["fileContent"] = aws_sdk_taxsettings.types.file_blob.serialize_json(
        value["file_content"]
    )
    return out


def deserialize_json(data: dict) -> TaxRegistrationDocFile:
    out: TaxRegistrationDocFile = {}  # type: ignore[typeddict-item]
    if "fileName" in data:
        out["file_name"] = data["fileName"]
    else:
        raise DeserializationError("TaxRegistrationDocFile.file_name required")
    if "fileContent" in data:
        import aws_sdk_taxsettings.types.file_blob

        out["file_content"] = aws_sdk_taxsettings.types.file_blob.deserialize_json(
            data["fileContent"]
        )
    else:
        raise DeserializationError("TaxRegistrationDocFile.file_content required")
    return out
