"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#CreateAssetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.__string
    import aws_sdk_mediapackage_vod.types.tags


class CreateAssetRequest(TypedDict):
    id: NotRequired["aws_sdk_mediapackage_vod.types.__string.__string"]
    """The unique identifier for the Asset."""
    packaging_group_id: NotRequired["aws_sdk_mediapackage_vod.types.__string.__string"]
    """The ID of the PackagingGroup for the Asset."""
    resource_id: NotRequired["aws_sdk_mediapackage_vod.types.__string.__string"]
    """The resource ID to include in SPEKE key requests."""
    source_arn: NotRequired["aws_sdk_mediapackage_vod.types.__string.__string"]
    """ARN of the source object in S3."""
    source_role_arn: NotRequired["aws_sdk_mediapackage_vod.types.__string.__string"]
    """The IAM role ARN used to access the source S3 bucket."""
    tags: NotRequired["aws_sdk_mediapackage_vod.types.tags.Tags"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssetRequest) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "packaging_group_id" in value:
        out["packagingGroupId"] = value["packaging_group_id"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "source_arn" in value:
        out["sourceArn"] = value["source_arn"]
    if "source_role_arn" in value:
        out["sourceRoleArn"] = value["source_role_arn"]
    if "tags" in value:
        import aws_sdk_mediapackage_vod.types.tags

        out["tags"] = aws_sdk_mediapackage_vod.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAssetRequest:
    out: CreateAssetRequest = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "packagingGroupId" in data:
        out["packaging_group_id"] = data["packagingGroupId"]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "sourceArn" in data:
        out["source_arn"] = data["sourceArn"]
    if "sourceRoleArn" in data:
        out["source_role_arn"] = data["sourceRoleArn"]
    if "tags" in data:
        import aws_sdk_mediapackage_vod.types.tags

        out["tags"] = aws_sdk_mediapackage_vod.types.tags.deserialize_json(data["tags"])
    return out
