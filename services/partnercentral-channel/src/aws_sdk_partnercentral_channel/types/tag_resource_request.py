"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_partnercentral_channel.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.tag_list
    import aws_sdk_partnercentral_channel.types.taggable_arn


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_partnercentral_channel.types.taggable_arn.TaggableArn"
    """<p>The Amazon Resource Name (ARN) of the resource to tag.</p>"""
    tags: "aws_sdk_partnercentral_channel.types.tag_list.TagList"
    """<p>Key-value pairs to associate with the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_partnercentral_channel.types.tag_list

    out["tags"] = aws_sdk_partnercentral_channel.types.tag_list.serialize_aws_json_1_0(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "tags" in data:
        import aws_sdk_partnercentral_channel.types.tag_list

        out["tags"] = (
            aws_sdk_partnercentral_channel.types.tag_list.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
