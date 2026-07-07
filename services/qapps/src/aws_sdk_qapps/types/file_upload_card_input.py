"""Generated from Smithy shape ``com.amazonaws.qapps#FileUploadCardInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.card_type
    import aws_sdk_qapps.types.filename
    import aws_sdk_qapps.types.title
    import aws_sdk_qapps.types.uuid


class FileUploadCardInput(TypedDict, closed=True):
    title: "aws_sdk_qapps.types.title.Title"
    """<p>The title or label of the file upload card.</p>"""
    id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the file upload card.</p>"""
    type: "aws_sdk_qapps.types.card_type.CardType"
    """<p>The type of the card.</p>"""
    filename: NotRequired["aws_sdk_qapps.types.filename.Filename"]
    """<p>The default filename to use for the file upload card.</p>"""
    file_id: NotRequired["aws_sdk_qapps.types.uuid.UUID"]
    """<p>The identifier of a pre-uploaded file associated with the card.</p>"""
    allow_override: NotRequired["bool"]
    """<p>A flag indicating if the user can override the default file for the upload card.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileUploadCardInput) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    out["id"] = value["id"]
    import aws_sdk_qapps.types.card_type

    out["type"] = aws_sdk_qapps.types.card_type.serialize_json(
        value.get("type", "file-upload")
    )
    if "filename" in value:
        out["filename"] = value["filename"]
    if "file_id" in value:
        out["fileId"] = value["file_id"]
    if "allow_override" in value:
        out["allowOverride"] = value["allow_override"]
    return out


def deserialize_json(data: dict) -> FileUploadCardInput:
    out: FileUploadCardInput = {}  # type: ignore[typeddict-item]
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("FileUploadCardInput.title required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("FileUploadCardInput.id required")
    if "type" in data:
        import aws_sdk_qapps.types.card_type

        out["type"] = aws_sdk_qapps.types.card_type.deserialize_json(data["type"])
    else:
        out["type"] = "file-upload"
    if "filename" in data:
        out["filename"] = data["filename"]
    if "fileId" in data:
        out["file_id"] = data["fileId"]
    if "allowOverride" in data:
        out["allow_override"] = data["allowOverride"]
    return out
