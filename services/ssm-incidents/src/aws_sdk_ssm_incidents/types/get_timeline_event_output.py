"""Generated from Smithy shape ``com.amazonaws.ssmincidents#GetTimelineEventOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.timeline_event


class GetTimelineEventOutput(TypedDict):
    event: "aws_sdk_ssm_incidents.types.timeline_event.TimelineEvent"
    """<p>Details about the timeline event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTimelineEventOutput) -> dict:
    out: dict = {}
    import aws_sdk_ssm_incidents.types.timeline_event

    out["event"] = aws_sdk_ssm_incidents.types.timeline_event.serialize_json(
        value["event"]
    )
    return out


def deserialize_json(data: dict) -> GetTimelineEventOutput:
    out: GetTimelineEventOutput = {}  # type: ignore[typeddict-item]
    if "event" in data:
        import aws_sdk_ssm_incidents.types.timeline_event

        out["event"] = aws_sdk_ssm_incidents.types.timeline_event.deserialize_json(
            data["event"]
        )
    else:
        raise DeserializationError("GetTimelineEventOutput.event required")
    return out
