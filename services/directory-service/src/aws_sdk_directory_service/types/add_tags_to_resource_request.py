"""Generated from Smithy shape ``com.amazonaws.directoryservice#AddTagsToResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.resource_id
    import aws_sdk_directory_service.types.tags


class AddTagsToResourceRequest(TypedDict):
    resource_id: "aws_sdk_directory_service.types.resource_id.ResourceId"
    """<p>Identifier (ID) for the directory to which to add the tag.</p>"""
    tags: "aws_sdk_directory_service.types.tags.Tags"
    """<p>The tags to be assigned to the directory.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddTagsToResourceRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    import aws_sdk_directory_service.types.tags

    out["Tags"] = aws_sdk_directory_service.types.tags.serialize_aws_json_1_1(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddTagsToResourceRequest:
    out: AddTagsToResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("AddTagsToResourceRequest.resource_id required")
    if "Tags" in data:
        import aws_sdk_directory_service.types.tags

        out["tags"] = aws_sdk_directory_service.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        raise DeserializationError("AddTagsToResourceRequest.tags required")
    return out
