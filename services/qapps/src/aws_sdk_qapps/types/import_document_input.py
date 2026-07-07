"""Generated from Smithy shape ``com.amazonaws.qapps#ImportDocumentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.document_scope
    import aws_sdk_qapps.types.filename
    import aws_sdk_qapps.types.instance_id
    import aws_sdk_qapps.types.uuid


class ImportDocumentInput(TypedDict, closed=True):
    instance_id: "aws_sdk_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    card_id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the card the file is associated with.</p>"""
    app_id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Q App the file is associated with.</p>"""
    file_contents_base64: "str"
    """<p>The base64-encoded contents of the file to upload.</p>"""
    file_name: "aws_sdk_qapps.types.filename.Filename"
    """<p>The name of the file being uploaded.</p>"""
    scope: "aws_sdk_qapps.types.document_scope.DocumentScope"
    """<p>Whether the file is associated with a Q App definition or a specific Q App session.</p>"""
    session_id: NotRequired["aws_sdk_qapps.types.uuid.UUID"]
    """<p>The unique identifier of the Q App session the file is associated with, if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportDocumentInput) -> dict:
    out: dict = {}
    out["cardId"] = value["card_id"]
    out["appId"] = value["app_id"]
    out["fileContentsBase64"] = value["file_contents_base64"]
    out["fileName"] = value["file_name"]
    import aws_sdk_qapps.types.document_scope

    out["scope"] = aws_sdk_qapps.types.document_scope.serialize_json(value["scope"])
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    return out


def deserialize_json(data: dict) -> ImportDocumentInput:
    out: ImportDocumentInput = {}  # type: ignore[typeddict-item]
    if "cardId" in data:
        out["card_id"] = data["cardId"]
    else:
        raise DeserializationError("ImportDocumentInput.card_id required")
    if "appId" in data:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("ImportDocumentInput.app_id required")
    if "fileContentsBase64" in data:
        out["file_contents_base64"] = data["fileContentsBase64"]
    else:
        raise DeserializationError("ImportDocumentInput.file_contents_base64 required")
    if "fileName" in data:
        out["file_name"] = data["fileName"]
    else:
        raise DeserializationError("ImportDocumentInput.file_name required")
    if "scope" in data:
        import aws_sdk_qapps.types.document_scope

        out["scope"] = aws_sdk_qapps.types.document_scope.deserialize_json(
            data["scope"]
        )
    else:
        raise DeserializationError("ImportDocumentInput.scope required")
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    return out
