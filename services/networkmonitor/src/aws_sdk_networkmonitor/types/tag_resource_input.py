"""Generated from Smithy shape ``com.amazonaws.networkmonitor#TagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_networkmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkmonitor.types.arn
    import aws_sdk_networkmonitor.types.tag_map


class TagResourceInput(TypedDict):
    resource_arn: "aws_sdk_networkmonitor.types.arn.Arn"
    """<p>The ARN of the monitor or probe to tag.</p>"""
    tags: "aws_sdk_networkmonitor.types.tag_map.TagMap"
    """<p>The list of key-value pairs assigned to the monitor or probe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import aws_sdk_networkmonitor.types.tag_map

    out["tags"] = aws_sdk_networkmonitor.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_networkmonitor.types.tag_map

        out["tags"] = aws_sdk_networkmonitor.types.tag_map.deserialize_json(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
