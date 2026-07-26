"""Generated from Smithy shape ``com.amazonaws.dlm#EventSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dlm.types.event_parameters
    import capo_dlm.types.event_source_values


class EventSource(TypedDict, closed=True):
    type: NotRequired["capo_dlm.types.event_source_values.EventSourceValues"]
    """<p>The source of the event. Currently only managed CloudWatch Events rules are supported.</p>"""
    parameters: NotRequired["capo_dlm.types.event_parameters.EventParameters"]
    """<p>Information about the event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventSource) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_dlm.types.event_source_values

        out["Type"] = capo_dlm.types.event_source_values.serialize_json(value["type"])
    if "parameters" in value:
        import capo_dlm.types.event_parameters

        out["Parameters"] = capo_dlm.types.event_parameters.serialize_json(
            value["parameters"]
        )
    return out


def deserialize_json(data: dict) -> EventSource:
    out: EventSource = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_dlm.types.event_source_values

        out["type"] = capo_dlm.types.event_source_values.deserialize_json(data["Type"])
    if "Parameters" in data:
        import capo_dlm.types.event_parameters

        out["parameters"] = capo_dlm.types.event_parameters.deserialize_json(
            data["Parameters"]
        )
    return out
