"""Generated from Smithy shape ``com.amazonaws.qapps#CreatePresignedUrlInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.document_scope
    import aws_sdk_qapps.types.filename
    import aws_sdk_qapps.types.instance_id
    import aws_sdk_qapps.types.uuid


class CreatePresignedUrlInput(TypedDict, closed=True):
    instance_id: "aws_sdk_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    card_id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the card the file is associated with.</p>"""
    app_id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Q App the file is associated with.</p>"""
    file_contents_sha256: "str"
    """<p>The Base64-encoded SHA-256 digest of the contents of the file to be uploaded.</p>"""
    file_name: "aws_sdk_qapps.types.filename.Filename"
    """<p>The name of the file to be uploaded.</p>"""
    scope: "aws_sdk_qapps.types.document_scope.DocumentScope"
    """<p>Whether the file is associated with a Q App definition or a specific Q App session.</p>"""
    session_id: NotRequired["aws_sdk_qapps.types.uuid.UUID"]
    """<p>The unique identifier of the Q App session the file is associated with, if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePresignedUrlInput) -> dict:
    out: dict = {}
    out["cardId"] = value["card_id"]
    out["appId"] = value["app_id"]
    out["fileContentsSha256"] = value["file_contents_sha256"]
    out["fileName"] = value["file_name"]
    import aws_sdk_qapps.types.document_scope

    out["scope"] = aws_sdk_qapps.types.document_scope.serialize_json(value["scope"])
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    return out


def deserialize_json(data: dict) -> CreatePresignedUrlInput:
    out: CreatePresignedUrlInput = {}  # type: ignore[typeddict-item]
    if "cardId" in data:
        out["card_id"] = data["cardId"]
    else:
        raise DeserializationError("CreatePresignedUrlInput.card_id required")
    if "appId" in data:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("CreatePresignedUrlInput.app_id required")
    if "fileContentsSha256" in data:
        out["file_contents_sha256"] = data["fileContentsSha256"]
    else:
        raise DeserializationError(
            "CreatePresignedUrlInput.file_contents_sha256 required"
        )
    if "fileName" in data:
        out["file_name"] = data["fileName"]
    else:
        raise DeserializationError("CreatePresignedUrlInput.file_name required")
    if "scope" in data:
        import aws_sdk_qapps.types.document_scope

        out["scope"] = aws_sdk_qapps.types.document_scope.deserialize_json(
            data["scope"]
        )
    else:
        raise DeserializationError("CreatePresignedUrlInput.scope required")
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    return out
