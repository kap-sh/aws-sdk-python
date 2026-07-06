"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ResourceTag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.string
    import aws_sdk_cloudtrail.types.tags_list


class ResourceTag(TypedDict, closed=True):
    resource_id: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>Specifies the ARN of the resource.</p>"""
    tags_list: NotRequired["aws_sdk_cloudtrail.types.tags_list.TagsList"]
    """<p>A list of tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceTag) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "tags_list" in value:
        import aws_sdk_cloudtrail.types.tags_list

        out["TagsList"] = aws_sdk_cloudtrail.types.tags_list.serialize_aws_json_1_1(
            value["tags_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceTag:
    out: ResourceTag = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "TagsList" in data:
        import aws_sdk_cloudtrail.types.tags_list

        out["tags_list"] = aws_sdk_cloudtrail.types.tags_list.deserialize_aws_json_1_1(
            data["TagsList"]
        )
    return out
