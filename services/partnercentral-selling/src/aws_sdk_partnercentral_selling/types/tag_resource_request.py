"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.tag_list
    import aws_sdk_partnercentral_selling.types.taggable_resource_arn


class TagResourceRequest(TypedDict):
    resource_arn: (
        "aws_sdk_partnercentral_selling.types.taggable_resource_arn.TaggableResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the resource that you want to tag.</p>"""
    tags: "aws_sdk_partnercentral_selling.types.tag_list.TagList"
    """<p>A map of the key-value pairs of the tag or tags to assign.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_partnercentral_selling.types.tag_list

    out["Tags"] = aws_sdk_partnercentral_selling.types.tag_list.serialize_aws_json_1_0(
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
        import aws_sdk_partnercentral_selling.types.tag_list

        out["tags"] = (
            aws_sdk_partnercentral_selling.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
