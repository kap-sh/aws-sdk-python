"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.amazon_resource_arn
    import aws_sdk_lookoutequipment.types.tag_list


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_lookoutequipment.types.amazon_resource_arn.AmazonResourceArn"
    """<p>The Amazon Resource Name (ARN) of the specific resource to which the tag should be associated. </p>"""
    tags: "aws_sdk_lookoutequipment.types.tag_list.TagList"
    """<p>The tag or tags to be associated with a specific resource. Both the tag key and value are specified. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_lookoutequipment.types.tag_list

    out["Tags"] = aws_sdk_lookoutequipment.types.tag_list.serialize_aws_json_1_0(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "Tags" in data:
        import aws_sdk_lookoutequipment.types.tag_list

        out["tags"] = aws_sdk_lookoutequipment.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
