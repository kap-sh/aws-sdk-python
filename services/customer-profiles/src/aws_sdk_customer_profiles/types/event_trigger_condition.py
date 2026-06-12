"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventTriggerCondition``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.event_trigger_dimensions
    import aws_sdk_customer_profiles.types.event_trigger_logical_operator


class EventTriggerCondition(TypedDict):
    event_trigger_dimensions: "aws_sdk_customer_profiles.types.event_trigger_dimensions.EventTriggerDimensions"
    """<p>A list of dimensions to be evaluated for the event.</p>"""
    logical_operator: "aws_sdk_customer_profiles.types.event_trigger_logical_operator.EventTriggerLogicalOperator"
    """<p>The operator used to combine multiple dimensions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventTriggerCondition) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.event_trigger_dimensions

    out["EventTriggerDimensions"] = (
        aws_sdk_customer_profiles.types.event_trigger_dimensions.serialize_json(
            value["event_trigger_dimensions"]
        )
    )
    import aws_sdk_customer_profiles.types.event_trigger_logical_operator

    out["LogicalOperator"] = (
        aws_sdk_customer_profiles.types.event_trigger_logical_operator.serialize_json(
            value["logical_operator"]
        )
    )
    return out


def deserialize_json(data: dict) -> EventTriggerCondition:
    out: EventTriggerCondition = {}  # type: ignore[typeddict-item]
    if "EventTriggerDimensions" in data:
        import aws_sdk_customer_profiles.types.event_trigger_dimensions

        out["event_trigger_dimensions"] = (
            aws_sdk_customer_profiles.types.event_trigger_dimensions.deserialize_json(
                data["EventTriggerDimensions"]
            )
        )
    else:
        raise DeserializationError(
            "EventTriggerCondition.event_trigger_dimensions required"
        )
    if "LogicalOperator" in data:
        import aws_sdk_customer_profiles.types.event_trigger_logical_operator

        out["logical_operator"] = (
            aws_sdk_customer_profiles.types.event_trigger_logical_operator.deserialize_json(
                data["LogicalOperator"]
            )
        )
    else:
        raise DeserializationError("EventTriggerCondition.logical_operator required")
    return out
