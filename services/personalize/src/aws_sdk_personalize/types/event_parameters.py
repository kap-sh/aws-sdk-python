"""Generated from Smithy shape ``com.amazonaws.personalize#EventParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.event_type
    import aws_sdk_personalize.types.event_type_threshold_value
    import aws_sdk_personalize.types.event_type_weight


class EventParameters(TypedDict):
    event_type: NotRequired["aws_sdk_personalize.types.event_type.EventType"]
    """<p>The name of the event type to be considered for solution creation.</p>"""
    event_value_threshold: NotRequired[
        "aws_sdk_personalize.types.event_type_threshold_value.EventTypeThresholdValue"
    ]
    """<p>The threshold of the event type. Only events with a value greater or equal to this threshold will be considered for solution creation.</p>"""
    weight: NotRequired["aws_sdk_personalize.types.event_type_weight.EventTypeWeight"]
    """<p>The weight of the event type. A higher weight means higher importance of the event type for the created solution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventParameters) -> dict:
    out: dict = {}
    if "event_type" in value:
        out["eventType"] = value["event_type"]
    if "event_value_threshold" in value:
        out["eventValueThreshold"] = value["event_value_threshold"]
    if "weight" in value:
        out["weight"] = value["weight"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EventParameters:
    out: EventParameters = {}  # type: ignore[typeddict-item]
    if "eventType" in data:
        out["event_type"] = data["eventType"]
    if "eventValueThreshold" in data:
        out["event_value_threshold"] = data["eventValueThreshold"]
    if "weight" in data:
        out["weight"] = data["weight"]
    return out
