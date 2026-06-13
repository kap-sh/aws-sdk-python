"""Generated from Smithy shape ``com.amazonaws.bedrock#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.tag_key_list
    import aws_sdk_bedrock.types.taggable_resources_arn


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_bedrock.types.taggable_resources_arn.TaggableResourcesArn"
    """<p>The Amazon Resource Name (ARN) of the resource to untag.</p>"""
    tag_keys: "aws_sdk_bedrock.types.tag_key_list.TagKeyList"
    """<p>Tag keys of the tags to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceARN"] = value["resource_arn"]
    import aws_sdk_bedrock.types.tag_key_list

    out["tagKeys"] = aws_sdk_bedrock.types.tag_key_list.serialize_json(
        value["tag_keys"]
    )
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceARN" in data:
        out["resource_arn"] = data["resourceARN"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "tagKeys" in data:
        import aws_sdk_bedrock.types.tag_key_list

        out["tag_keys"] = aws_sdk_bedrock.types.tag_key_list.deserialize_json(
            data["tagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
