"""Generated from Smithy shape ``com.amazonaws.directconnect#ResourceTag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.resource_arn
    import aws_sdk_direct_connect.types.tag_list


class ResourceTag(TypedDict, closed=True):
    resource_arn: NotRequired["aws_sdk_direct_connect.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tags: NotRequired["aws_sdk_direct_connect.types.tag_list.TagList"]
    """<p>The tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceTag) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "tags" in value:
        import aws_sdk_direct_connect.types.tag_list

        out["tags"] = aws_sdk_direct_connect.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceTag:
    out: ResourceTag = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "tags" in data:
        import aws_sdk_direct_connect.types.tag_list

        out["tags"] = aws_sdk_direct_connect.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
