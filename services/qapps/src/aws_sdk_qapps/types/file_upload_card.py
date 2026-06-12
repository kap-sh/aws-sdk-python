"""Generated from Smithy shape ``com.amazonaws.qapps#FileUploadCard``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.card_type
    import aws_sdk_qapps.types.dependency_list
    import aws_sdk_qapps.types.title
    import aws_sdk_qapps.types.uuid


class FileUploadCard(TypedDict):
    id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the file upload card.</p>"""
    title: "aws_sdk_qapps.types.title.Title"
    """<p>The title of the file upload card.</p>"""
    dependencies: "aws_sdk_qapps.types.dependency_list.DependencyList"
    """<p>Any dependencies or requirements for the file upload card.</p>"""
    type: "aws_sdk_qapps.types.card_type.CardType"
    """<p>The type of the card.</p>"""
    filename: NotRequired["str"]
    """<p>The name of the file being uploaded.</p>"""
    file_id: NotRequired["str"]
    """<p>The unique identifier of the file associated with the card.</p>"""
    allow_override: NotRequired["bool"]
    """<p>A flag indicating if the user can override the default file for the upload card.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileUploadCard) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["title"] = value["title"]
    import aws_sdk_qapps.types.dependency_list

    out["dependencies"] = aws_sdk_qapps.types.dependency_list.serialize_json(
        value["dependencies"]
    )
    import aws_sdk_qapps.types.card_type

    out["type"] = aws_sdk_qapps.types.card_type.serialize_json(value["type"])
    if "filename" in value:
        out["filename"] = value["filename"]
    if "file_id" in value:
        out["fileId"] = value["file_id"]
    if "allow_override" in value:
        out["allowOverride"] = value["allow_override"]
    return out


def deserialize_json(data: dict) -> FileUploadCard:
    out: FileUploadCard = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("FileUploadCard.id required")
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("FileUploadCard.title required")
    if "dependencies" in data:
        import aws_sdk_qapps.types.dependency_list

        out["dependencies"] = aws_sdk_qapps.types.dependency_list.deserialize_json(
            data["dependencies"]
        )
    else:
        raise DeserializationError("FileUploadCard.dependencies required")
    if "type" in data:
        import aws_sdk_qapps.types.card_type

        out["type"] = aws_sdk_qapps.types.card_type.deserialize_json(data["type"])
    else:
        raise DeserializationError("FileUploadCard.type required")
    if "filename" in data:
        out["filename"] = data["filename"]
    if "fileId" in data:
        out["file_id"] = data["fileId"]
    if "allowOverride" in data:
        out["allow_override"] = data["allowOverride"]
    return out
