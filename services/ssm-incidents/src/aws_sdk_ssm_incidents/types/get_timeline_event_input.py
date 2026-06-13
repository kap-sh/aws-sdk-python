"""Generated from Smithy shape ``com.amazonaws.ssmincidents#GetTimelineEventInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.arn
    import aws_sdk_ssm_incidents.types.uuid


class GetTimelineEventInput(TypedDict):
    incident_record_arn: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the incident that includes the timeline event.</p>"""
    event_id: "aws_sdk_ssm_incidents.types.uuid.UUID"
    """<p>The ID of the event. You can get an event's ID when you create it, or by using <code>ListTimelineEvents</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTimelineEventInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTimelineEventInput:
    out: GetTimelineEventInput = {}  # type: ignore[typeddict-item]
    return out
