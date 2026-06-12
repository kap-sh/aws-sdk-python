"""Generated from Smithy shape ``com.amazonaws.appconfig#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_appconfig.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.arn
    import aws_sdk_appconfig.types.tag_map


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_appconfig.types.arn.Arn"
    """<p>The ARN of the resource for which to retrieve tags.</p>"""
    tags: "aws_sdk_appconfig.types.tag_map.TagMap"
    """<p>The key-value string map. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with <code>aws:</code>. The tag value can be up to 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_appconfig.types.tag_map

    out["Tags"] = aws_sdk_appconfig.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_appconfig.types.tag_map

        out["tags"] = aws_sdk_appconfig.types.tag_map.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
