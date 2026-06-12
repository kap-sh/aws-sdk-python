"""Generated from Smithy shape ``com.amazonaws.directoryservice#RemoveTagsFromResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.resource_id
    import aws_sdk_directory_service.types.tag_keys


class RemoveTagsFromResourceRequest(TypedDict):
    resource_id: "aws_sdk_directory_service.types.resource_id.ResourceId"
    """<p>Identifier (ID) of the directory from which to remove the tag.</p>"""
    tag_keys: "aws_sdk_directory_service.types.tag_keys.TagKeys"
    """<p>The tag key (name) of the tag to be removed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveTagsFromResourceRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    import aws_sdk_directory_service.types.tag_keys

    out["TagKeys"] = aws_sdk_directory_service.types.tag_keys.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveTagsFromResourceRequest:
    out: RemoveTagsFromResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("RemoveTagsFromResourceRequest.resource_id required")
    if "TagKeys" in data:
        import aws_sdk_directory_service.types.tag_keys

        out["tag_keys"] = (
            aws_sdk_directory_service.types.tag_keys.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("RemoveTagsFromResourceRequest.tag_keys required")
    return out
