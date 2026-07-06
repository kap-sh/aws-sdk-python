"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.double
    import aws_sdk_customer_profiles.types.event_parameters_event_type_string
    import aws_sdk_customer_profiles.types.event_parameters_event_weight_double


class EventParameters(TypedDict, closed=True):
    event_type: "aws_sdk_customer_profiles.types.event_parameters_event_type_string.EventParametersEventTypeString"
    """<p>The type of event being tracked (e.g., 'click', 'purchase', 'view').</p>"""
    event_value_threshold: NotRequired["aws_sdk_customer_profiles.types.double.Double"]
    """<p>The minimum value threshold that an event must meet to be considered valid.</p>"""
    event_weight: NotRequired[
        "aws_sdk_customer_profiles.types.event_parameters_event_weight_double.EventParametersEventWeightDouble"
    ]
    """<p>The weight of the event type. A higher weight means higher importance of the event type for the created solution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventParameters) -> dict:
    out: dict = {}
    out["EventType"] = value["event_type"]
    if "event_value_threshold" in value:
        out["EventValueThreshold"] = value["event_value_threshold"]
    if "event_weight" in value:
        out["EventWeight"] = value["event_weight"]
    return out


def deserialize_json(data: dict) -> EventParameters:
    out: EventParameters = {}  # type: ignore[typeddict-item]
    if "EventType" in data:
        out["event_type"] = data["EventType"]
    else:
        raise DeserializationError("EventParameters.event_type required")
    if "EventValueThreshold" in data:
        out["event_value_threshold"] = data["EventValueThreshold"]
    if "EventWeight" in data:
        out["event_weight"] = data["EventWeight"]
    return out
