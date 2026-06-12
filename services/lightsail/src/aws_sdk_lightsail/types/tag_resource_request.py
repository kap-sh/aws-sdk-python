"""Generated from Smithy shape ``com.amazonaws.lightsail#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_arn
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.tag_list


class TagResourceRequest(TypedDict):
    resource_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the resource to which you are adding tags.</p>"""
    resource_arn: NotRequired["aws_sdk_lightsail.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the resource to which you want to add a tag.</p>"""
    tags: "aws_sdk_lightsail.types.tag_list.TagList"
    """<p>The tag key and optional value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceName"] = value["resource_name"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    import aws_sdk_lightsail.types.tag_list

    out["tags"] = aws_sdk_lightsail.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    else:
        raise DeserializationError("TagResourceRequest.resource_name required")
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "tags" in data:
        import aws_sdk_lightsail.types.tag_list

        out["tags"] = aws_sdk_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
