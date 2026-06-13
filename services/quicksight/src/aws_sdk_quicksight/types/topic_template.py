"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicTemplate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.limited_string
    import aws_sdk_quicksight.types.slots


class TopicTemplate(TypedDict):
    template_type: NotRequired["aws_sdk_quicksight.types.limited_string.LimitedString"]
    """<p>The template type for the <code>TopicTemplate</code>.</p>"""
    slots: NotRequired["aws_sdk_quicksight.types.slots.Slots"]
    """<p>The slots for the <code>TopicTemplate</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicTemplate) -> dict:
    out: dict = {}
    if "template_type" in value:
        out["TemplateType"] = value["template_type"]
    if "slots" in value:
        import aws_sdk_quicksight.types.slots

        out["Slots"] = aws_sdk_quicksight.types.slots.serialize_json(value["slots"])
    return out


def deserialize_json(data: dict) -> TopicTemplate:
    out: TopicTemplate = {}  # type: ignore[typeddict-item]
    if "TemplateType" in data:
        out["template_type"] = data["TemplateType"]
    if "Slots" in data:
        import aws_sdk_quicksight.types.slots

        out["slots"] = aws_sdk_quicksight.types.slots.deserialize_json(data["Slots"])
    return out
