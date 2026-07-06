"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventTriggerSummaryItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.tag_map
    import aws_sdk_customer_profiles.types.text
    import aws_sdk_customer_profiles.types.timestamp
    import aws_sdk_customer_profiles.types.type_name


class EventTriggerSummaryItem(TypedDict, closed=True):
    object_type_name: NotRequired["aws_sdk_customer_profiles.types.type_name.typeName"]
    """<p>The unique name of the object type.</p>"""
    event_trigger_name: NotRequired["aws_sdk_customer_profiles.types.name.name"]
    """<p>The unique name of the event trigger.</p>"""
    description: NotRequired["aws_sdk_customer_profiles.types.text.text"]
    """<p>The description of the event trigger.</p>"""
    created_at: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the event trigger was created.</p>"""
    last_updated_at: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the event trigger was most recently updated.</p>"""
    tags: NotRequired["aws_sdk_customer_profiles.types.tag_map.TagMap"]
    """<p>An array of key-value pairs to apply to this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventTriggerSummaryItem) -> dict:
    out: dict = {}
    if "object_type_name" in value:
        out["ObjectTypeName"] = value["object_type_name"]
    if "event_trigger_name" in value:
        out["EventTriggerName"] = value["event_trigger_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_at" in value:
        import aws_sdk_customer_profiles.types.timestamp

        out["CreatedAt"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_customer_profiles.types.timestamp

        out["LastUpdatedAt"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "tags" in value:
        import aws_sdk_customer_profiles.types.tag_map

        out["Tags"] = aws_sdk_customer_profiles.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> EventTriggerSummaryItem:
    out: EventTriggerSummaryItem = {}  # type: ignore[typeddict-item]
    if "ObjectTypeName" in data:
        out["object_type_name"] = data["ObjectTypeName"]
    if "EventTriggerName" in data:
        out["event_trigger_name"] = data["EventTriggerName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedAt" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["created_at"] = aws_sdk_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "LastUpdatedAt" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            aws_sdk_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    if "Tags" in data:
        import aws_sdk_customer_profiles.types.tag_map

        out["tags"] = aws_sdk_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
