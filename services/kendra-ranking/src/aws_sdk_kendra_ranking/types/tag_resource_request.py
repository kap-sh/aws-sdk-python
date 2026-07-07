"""Generated from Smithy shape ``com.amazonaws.kendraranking#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kendra_ranking.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra_ranking.types.amazon_resource_name
    import aws_sdk_kendra_ranking.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_kendra_ranking.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the rescore execution plan to tag.</p>"""
    tags: "aws_sdk_kendra_ranking.types.tag_list.TagList"
    """<p>A list of tag keys to add to a rescore execution plan. If a tag already exists, the existing value is replaced with the new value.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import aws_sdk_kendra_ranking.types.tag_list

    out["Tags"] = aws_sdk_kendra_ranking.types.tag_list.serialize_aws_json_1_0(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "Tags" in data:
        import aws_sdk_kendra_ranking.types.tag_list

        out["tags"] = aws_sdk_kendra_ranking.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
