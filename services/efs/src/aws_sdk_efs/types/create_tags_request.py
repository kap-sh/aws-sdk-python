"""Generated from Smithy shape ``com.amazonaws.efs#CreateTagsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_efs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_efs.types.file_system_id
    import aws_sdk_efs.types.tags


class CreateTagsRequest(TypedDict):
    file_system_id: "aws_sdk_efs.types.file_system_id.FileSystemId"
    """<p>The ID of the file system whose tags you want to modify (String). This operation modifies the tags only, not the file system.</p>"""
    tags: "aws_sdk_efs.types.tags.Tags"
    """<p>An array of <code>Tag</code> objects to add. Each <code>Tag</code> object is a key-value pair. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTagsRequest) -> dict:
    out: dict = {}
    import aws_sdk_efs.types.tags

    out["Tags"] = aws_sdk_efs.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateTagsRequest:
    out: CreateTagsRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_efs.types.tags

        out["tags"] = aws_sdk_efs.types.tags.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("CreateTagsRequest.tags required")
    return out
