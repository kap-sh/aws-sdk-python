"""Generated from Smithy shape ``com.amazonaws.appsync#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appsync.types.resource_arn
    import aws_sdk_appsync.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_appsync.types.resource_arn.ResourceArn"
    """<p>The <code>GraphqlApi</code> Amazon Resource Name (ARN).</p>"""
    tags: "aws_sdk_appsync.types.tag_map.TagMap"
    """<p>A <code>TagMap</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_appsync.types.tag_map

    out["tags"] = aws_sdk_appsync.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_appsync.types.tag_map

        out["tags"] = aws_sdk_appsync.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
