"""Generated from Smithy shape ``com.amazonaws.internetmonitor#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_internetmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_internetmonitor.types.monitor_arn
    import aws_sdk_internetmonitor.types.tag_map


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_internetmonitor.types.monitor_arn.MonitorArn"
    """<p>The Amazon Resource Name (ARN) for a tag that you add to a resource. Tags are supported only for monitors in Amazon CloudWatch Internet Monitor.</p>"""
    tags: "aws_sdk_internetmonitor.types.tag_map.TagMap"
    """<p>Tags that you add to a resource. You can add a maximum of 50 tags in Internet Monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import aws_sdk_internetmonitor.types.tag_map

    out["Tags"] = aws_sdk_internetmonitor.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_internetmonitor.types.tag_map

        out["tags"] = aws_sdk_internetmonitor.types.tag_map.deserialize_json(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
