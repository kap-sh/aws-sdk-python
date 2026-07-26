"""Generated from Smithy shape ``com.amazonaws.ssmincidents#GetTimelineEventOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_incidents.types.timeline_event


class GetTimelineEventOutput(TypedDict, closed=True):
    event: "capo_ssm_incidents.types.timeline_event.TimelineEvent"
    """<p>Details about the timeline event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTimelineEventOutput) -> dict:
    out: dict = {}
    import capo_ssm_incidents.types.timeline_event

    out["event"] = capo_ssm_incidents.types.timeline_event.serialize_json(
        value["event"]
    )
    return out


def deserialize_json(data: dict) -> GetTimelineEventOutput:
    out: GetTimelineEventOutput = {}  # type: ignore[typeddict-item]
    if "event" in data:
        import capo_ssm_incidents.types.timeline_event

        out["event"] = capo_ssm_incidents.types.timeline_event.deserialize_json(
            data["event"]
        )
    else:
        raise DeserializationError("GetTimelineEventOutput.event required")
    return out
