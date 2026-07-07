"""Generated from Smithy shape ``com.amazonaws.efs#DeleteTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_efs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_efs.types.file_system_id
    import aws_sdk_efs.types.tag_keys


class DeleteTagsRequest(TypedDict, closed=True):
    file_system_id: "aws_sdk_efs.types.file_system_id.FileSystemId"
    """<p>The ID of the file system whose tags you want to delete (String).</p>"""
    tag_keys: "aws_sdk_efs.types.tag_keys.TagKeys"
    """<p>A list of tag keys to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTagsRequest) -> dict:
    out: dict = {}
    import aws_sdk_efs.types.tag_keys

    out["TagKeys"] = aws_sdk_efs.types.tag_keys.serialize_json(value["tag_keys"])
    return out


def deserialize_json(data: dict) -> DeleteTagsRequest:
    out: DeleteTagsRequest = {}  # type: ignore[typeddict-item]
    if "TagKeys" in data:
        import aws_sdk_efs.types.tag_keys

        out["tag_keys"] = aws_sdk_efs.types.tag_keys.deserialize_json(data["TagKeys"])
    else:
        raise DeserializationError("DeleteTagsRequest.tag_keys required")
    return out
