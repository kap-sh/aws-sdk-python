"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_partnercentral_benefits.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.tag_key_list
    import aws_sdk_partnercentral_benefits.types.taggable_resource_arn


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_partnercentral_benefits.types.taggable_resource_arn.TaggableResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource to remove tags from.</p>"""
    tag_keys: "aws_sdk_partnercentral_benefits.types.tag_key_list.TagKeyList"
    """<p>A list of tag keys to remove from the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_partnercentral_benefits.types.tag_key_list

    out["tagKeys"] = (
        aws_sdk_partnercentral_benefits.types.tag_key_list.serialize_aws_json_1_0(
            value["tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "tagKeys" in data:
        import aws_sdk_partnercentral_benefits.types.tag_key_list

        out["tag_keys"] = (
            aws_sdk_partnercentral_benefits.types.tag_key_list.deserialize_aws_json_1_0(
                data["tagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
