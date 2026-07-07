"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateEventTriggerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.event_trigger_conditions
    import aws_sdk_customer_profiles.types.event_trigger_limits
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.sensitive_text
    import aws_sdk_customer_profiles.types.tag_map
    import aws_sdk_customer_profiles.types.type_name


class CreateEventTriggerRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    event_trigger_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the event trigger.</p>"""
    object_type_name: "aws_sdk_customer_profiles.types.type_name.typeName"
    """<p>The unique name of the object type.</p>"""
    description: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_text.sensitiveText"
    ]
    """<p>The description of the event trigger.</p>"""
    event_trigger_conditions: "aws_sdk_customer_profiles.types.event_trigger_conditions.EventTriggerConditions"
    """<p>A list of conditions that determine when an event should trigger the destination.</p>"""
    segment_filter: NotRequired["aws_sdk_customer_profiles.types.name.name"]
    """<p>The destination is triggered only for profiles that meet the criteria of a segment definition.</p>"""
    event_trigger_limits: NotRequired[
        "aws_sdk_customer_profiles.types.event_trigger_limits.EventTriggerLimits"
    ]
    """<p>Defines limits controlling whether an event triggers the destination, based on ingestion latency and the number of invocations per profile over specific time periods.</p>"""
    tags: NotRequired["aws_sdk_customer_profiles.types.tag_map.TagMap"]
    """<p>An array of key-value pairs to apply to this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEventTriggerRequest) -> dict:
    out: dict = {}
    out["ObjectTypeName"] = value["object_type_name"]
    if "description" in value:
        out["Description"] = value["description"]
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
    if "tags" in value:
        import aws_sdk_customer_profiles.types.tag_map

        out["Tags"] = aws_sdk_customer_profiles.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateEventTriggerRequest:
    out: CreateEventTriggerRequest = {}  # type: ignore[typeddict-item]
    if "ObjectTypeName" in data:
        out["object_type_name"] = data["ObjectTypeName"]
    else:
        raise DeserializationError(
            "CreateEventTriggerRequest.object_type_name required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "EventTriggerConditions" in data:
        import aws_sdk_customer_profiles.types.event_trigger_conditions

        out["event_trigger_conditions"] = (
            aws_sdk_customer_profiles.types.event_trigger_conditions.deserialize_json(
                data["EventTriggerConditions"]
            )
        )
    else:
        raise DeserializationError(
            "CreateEventTriggerRequest.event_trigger_conditions required"
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
    if "Tags" in data:
        import aws_sdk_customer_profiles.types.tag_map

        out["tags"] = aws_sdk_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
