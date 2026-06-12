"""Generated from Smithy shape ``com.amazonaws.scheduler#TagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_scheduler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_scheduler.types.tag_list
    import aws_sdk_scheduler.types.tag_resource_arn


class TagResourceInput(TypedDict):
    resource_arn: "aws_sdk_scheduler.types.tag_resource_arn.TagResourceArn"
    """<p>The Amazon Resource Name (ARN) of the schedule group that you are adding tags to.</p>"""
    tags: "aws_sdk_scheduler.types.tag_list.TagList"
    """<p>The list of tags to associate with the schedule group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import aws_sdk_scheduler.types.tag_list

    out["Tags"] = aws_sdk_scheduler.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_scheduler.types.tag_list

        out["tags"] = aws_sdk_scheduler.types.tag_list.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
