"""Generated from Smithy shape ``com.amazonaws.fms#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_fms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fms.types.resource_arn
    import aws_sdk_fms.types.tag_list


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_fms.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource to return tags for. The Firewall Manager resources that support tagging are policies, applications lists, and protocols lists. </p>"""
    tag_list: "aws_sdk_fms.types.tag_list.TagList"
    """<p>The tags to add to the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_fms.types.tag_list

    out["TagList"] = aws_sdk_fms.types.tag_list.serialize_aws_json_1_1(
        value["tag_list"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "TagList" in data:
        import aws_sdk_fms.types.tag_list

        out["tag_list"] = aws_sdk_fms.types.tag_list.deserialize_aws_json_1_1(
            data["TagList"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tag_list required")
    return out
