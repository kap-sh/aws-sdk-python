"""Generated from Smithy shape ``com.amazonaws.kendraranking#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kendra_ranking.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra_ranking.types.amazon_resource_name
    import aws_sdk_kendra_ranking.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_kendra_ranking.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the rescore execution plan to remove the tag.</p>"""
    tag_keys: "aws_sdk_kendra_ranking.types.tag_key_list.TagKeyList"
    """<p>A list of tag keys to remove from the rescore execution plan. If a tag key does not exist on the resource, it is ignored.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import aws_sdk_kendra_ranking.types.tag_key_list

    out["TagKeys"] = aws_sdk_kendra_ranking.types.tag_key_list.serialize_aws_json_1_0(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "TagKeys" in data:
        import aws_sdk_kendra_ranking.types.tag_key_list

        out["tag_keys"] = (
            aws_sdk_kendra_ranking.types.tag_key_list.deserialize_aws_json_1_0(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
