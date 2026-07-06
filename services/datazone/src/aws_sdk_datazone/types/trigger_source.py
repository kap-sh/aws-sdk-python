"""Generated from Smithy shape ``com.amazonaws.datazone#TriggerSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.trigger_source_type


class TriggerSource(TypedDict, closed=True):
    type: NotRequired["aws_sdk_datazone.types.trigger_source_type.TriggerSourceType"]
    """<p>The type of the trigger source. Valid values are <code>MANUAL</code>, <code>SCHEDULED</code>, and <code>WORKFLOW</code>.</p>"""
    name: NotRequired["str"]
    """<p>The name of the trigger source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TriggerSource) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_datazone.types.trigger_source_type

        out["type"] = aws_sdk_datazone.types.trigger_source_type.serialize_json(
            value["type"]
        )
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> TriggerSource:
    out: TriggerSource = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_datazone.types.trigger_source_type

        out["type"] = aws_sdk_datazone.types.trigger_source_type.deserialize_json(
            data["type"]
        )
    if "name" in data:
        out["name"] = data["name"]
    return out
