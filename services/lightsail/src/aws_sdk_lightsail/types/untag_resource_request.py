"""Generated from Smithy shape ``com.amazonaws.lightsail#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_arn
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the resource from which you are removing a tag.</p>"""
    resource_arn: NotRequired["aws_sdk_lightsail.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the resource from which you want to remove a tag.</p>"""
    tag_keys: "aws_sdk_lightsail.types.tag_key_list.TagKeyList"
    """<p>The tag keys to delete from the specified resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceName"] = value["resource_name"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    import aws_sdk_lightsail.types.tag_key_list

    out["tagKeys"] = aws_sdk_lightsail.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_name required")
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "tagKeys" in data:
        import aws_sdk_lightsail.types.tag_key_list

        out["tag_keys"] = aws_sdk_lightsail.types.tag_key_list.deserialize_aws_json_1_1(
            data["tagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
