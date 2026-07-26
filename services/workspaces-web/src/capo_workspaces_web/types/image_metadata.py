"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ImageMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_web.types.mime_type
    import capo_workspaces_web.types.string_type
    import capo_workspaces_web.types.timestamp


class ImageMetadata(TypedDict, closed=True):
    mime_type: "capo_workspaces_web.types.mime_type.MimeType"
    """<p>The MIME type of the image.</p>"""
    file_extension: "capo_workspaces_web.types.string_type.StringType"
    """<p>The file extension of the image.</p>"""
    last_upload_timestamp: "capo_workspaces_web.types.timestamp.Timestamp"
    """<p>The timestamp when the image was last uploaded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageMetadata) -> dict:
    out: dict = {}
    import capo_workspaces_web.types.mime_type

    out["mimeType"] = capo_workspaces_web.types.mime_type.serialize_json(
        value["mime_type"]
    )
    out["fileExtension"] = value["file_extension"]
    import capo_workspaces_web.types.timestamp

    out["lastUploadTimestamp"] = capo_workspaces_web.types.timestamp.serialize_json(
        value["last_upload_timestamp"]
    )
    return out


def deserialize_json(data: dict) -> ImageMetadata:
    out: ImageMetadata = {}  # type: ignore[typeddict-item]
    if "mimeType" in data:
        import capo_workspaces_web.types.mime_type

        out["mime_type"] = capo_workspaces_web.types.mime_type.deserialize_json(
            data["mimeType"]
        )
    else:
        raise DeserializationError("ImageMetadata.mime_type required")
    if "fileExtension" in data:
        out["file_extension"] = data["fileExtension"]
    else:
        raise DeserializationError("ImageMetadata.file_extension required")
    if "lastUploadTimestamp" in data:
        import capo_workspaces_web.types.timestamp

        out["last_upload_timestamp"] = (
            capo_workspaces_web.types.timestamp.deserialize_json(
                data["lastUploadTimestamp"]
            )
        )
    else:
        raise DeserializationError("ImageMetadata.last_upload_timestamp required")
    return out
