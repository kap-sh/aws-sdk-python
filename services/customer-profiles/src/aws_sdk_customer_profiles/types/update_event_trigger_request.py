"""Generated from Smithy shape ``com.amazonaws.customerprofiles#UpdateEventTriggerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.event_trigger_conditions
    import aws_sdk_customer_profiles.types.event_trigger_limits
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.sensitive_text
    import aws_sdk_customer_profiles.types.type_name


class UpdateEventTriggerRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    event_trigger_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the event trigger.</p>"""
    object_type_name: NotRequired["aws_sdk_customer_profiles.types.type_name.typeName"]
    """<p>The unique name of the object type.</p>"""
    description: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_text.sensitiveText"
    ]
    """<p>The description of the event trigger.</p>"""
    event_trigger_conditions: NotRequired[
        "aws_sdk_customer_profiles.types.event_trigger_conditions.EventTriggerConditions"
    ]
    """<p>A list of conditions that determine when an event should trigger the destination.</p>"""
    segment_filter: NotRequired["aws_sdk_customer_profiles.types.name.name"]
    """<p>The destination is triggered only for profiles that meet the criteria of a segment definition.</p>"""
    event_trigger_limits: NotRequired[
        "aws_sdk_customer_profiles.types.event_trigger_limits.EventTriggerLimits"
    ]
    """<p>Defines limits controlling whether an event triggers the destination, based on ingestion latency and the number of invocations per profile over specific time periods.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEventTriggerRequest) -> dict:
    out: dict = {}
    if "object_type_name" in value:
        out["ObjectTypeName"] = value["object_type_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "event_trigger_conditions" in value:
        import aws_sdk_customer_profiles.types.event_trigger_conditions

        out["EventTriggerConditions"] = (
            aws_sdk_customer_profiles.types.event_trigger_conditions.serialize_json(
                value["event_trigger_conditions"]
            )
        )
    if "segment_filter" in value:
        out["SegmentFilter"] = value["segment_filter"]
    if "event_trigger_limits" in value:
        import aws_sdk_customer_profiles.types.event_trigger_limits

        out["EventTriggerLimits"] = (
            aws_sdk_customer_profiles.types.event_trigger_limits.serialize_json(
                value["event_trigger_limits"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateEventTriggerRequest:
    out: UpdateEventTriggerRequest = {}  # type: ignore[typeddict-item]
    if "ObjectTypeName" in data:
        out["object_type_name"] = data["ObjectTypeName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "EventTriggerConditions" in data:
        import aws_sdk_customer_profiles.types.event_trigger_conditions

        out["event_trigger_conditions"] = (
            aws_sdk_customer_profiles.types.event_trigger_conditions.deserialize_json(
                data["EventTriggerConditions"]
            )
        )
    if "SegmentFilter" in data:
        out["segment_filter"] = data["SegmentFilter"]
    if "EventTriggerLimits" in data:
        import aws_sdk_customer_profiles.types.event_trigger_limits

        out["event_trigger_limits"] = (
            aws_sdk_customer_profiles.types.event_trigger_limits.deserialize_json(
                data["EventTriggerLimits"]
            )
        )
    return out
