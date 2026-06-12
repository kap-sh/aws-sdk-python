"""Generated from Smithy shape ``com.amazonaws.translate#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_translate.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_translate.types.resource_arn
    import aws_sdk_translate.types.tag_list


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_translate.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the given Amazon Translate resource to which you want to associate the tags. </p>"""
    tags: "aws_sdk_translate.types.tag_list.TagList"
    """<p>Tags being associated with a specific Amazon Translate resource. There can be a maximum of 50 tags (both existing and pending) associated with a specific resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_translate.types.tag_list

    out["Tags"] = aws_sdk_translate.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "Tags" in data:
        import aws_sdk_translate.types.tag_list

        out["tags"] = aws_sdk_translate.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
