"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.amazon_resource_name
    import aws_sdk_lex_models_v2.types.tag_map


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_lex_models_v2.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the bot, bot alias, or bot channel to tag.</p>"""
    tags: "aws_sdk_lex_models_v2.types.tag_map.TagMap"
    """<p>A list of tag keys to add to the resource. If a tag key already exists, the existing value is replaced with the new value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.tag_map

    out["tags"] = aws_sdk_lex_models_v2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_lex_models_v2.types.tag_map

        out["tags"] = aws_sdk_lex_models_v2.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
