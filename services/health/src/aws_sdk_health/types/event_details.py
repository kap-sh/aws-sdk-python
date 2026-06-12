"""Generated from Smithy shape ``com.amazonaws.health#EventDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_health.types.event
    import aws_sdk_health.types.event_description
    import aws_sdk_health.types.event_metadata


class EventDetails(TypedDict):
    event: NotRequired["aws_sdk_health.types.event.Event"]
    """<p>Summary information about the event.</p>"""
    event_description: NotRequired[
        "aws_sdk_health.types.event_description.EventDescription"
    ]
    """<p>The most recent description of the event.</p>"""
    event_metadata: NotRequired["aws_sdk_health.types.event_metadata.eventMetadata"]
    """<p>Additional metadata about the event.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventDetails) -> dict:
    out: dict = {}
    if "event" in value:
        import aws_sdk_health.types.event

        out["event"] = aws_sdk_health.types.event.serialize_aws_json_1_1(value["event"])
    if "event_description" in value:
        import aws_sdk_health.types.event_description

        out["eventDescription"] = (
            aws_sdk_health.types.event_description.serialize_aws_json_1_1(
                value["event_description"]
            )
        )
    if "event_metadata" in value:
        import aws_sdk_health.types.event_metadata

        out["eventMetadata"] = (
            aws_sdk_health.types.event_metadata.serialize_aws_json_1_1(
                value["event_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EventDetails:
    out: EventDetails = {}  # type: ignore[typeddict-item]
    if "event" in data:
        import aws_sdk_health.types.event

        out["event"] = aws_sdk_health.types.event.deserialize_aws_json_1_1(
            data["event"]
        )
    if "eventDescription" in data:
        import aws_sdk_health.types.event_description

        out["event_description"] = (
            aws_sdk_health.types.event_description.deserialize_aws_json_1_1(
                data["eventDescription"]
            )
        )
    if "eventMetadata" in data:
        import aws_sdk_health.types.event_metadata

        out["event_metadata"] = (
            aws_sdk_health.types.event_metadata.deserialize_aws_json_1_1(
                data["eventMetadata"]
            )
        )
    return out
