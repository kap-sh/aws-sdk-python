"""Generated from Smithy shape ``com.amazonaws.dlm#EventSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dlm.types.event_parameters
    import aws_sdk_dlm.types.event_source_values


class EventSource(TypedDict):
    type: NotRequired["aws_sdk_dlm.types.event_source_values.EventSourceValues"]
    """<p>The source of the event. Currently only managed CloudWatch Events rules are supported.</p>"""
    parameters: NotRequired["aws_sdk_dlm.types.event_parameters.EventParameters"]
    """<p>Information about the event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventSource) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_dlm.types.event_source_values

        out["Type"] = aws_sdk_dlm.types.event_source_values.serialize_json(
            value["type"]
        )
    if "parameters" in value:
        import aws_sdk_dlm.types.event_parameters

        out["Parameters"] = aws_sdk_dlm.types.event_parameters.serialize_json(
            value["parameters"]
        )
    return out


def deserialize_json(data: dict) -> EventSource:
    out: EventSource = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_dlm.types.event_source_values

        out["type"] = aws_sdk_dlm.types.event_source_values.deserialize_json(
            data["Type"]
        )
    if "Parameters" in data:
        import aws_sdk_dlm.types.event_parameters

        out["parameters"] = aws_sdk_dlm.types.event_parameters.deserialize_json(
            data["Parameters"]
        )
    return out
