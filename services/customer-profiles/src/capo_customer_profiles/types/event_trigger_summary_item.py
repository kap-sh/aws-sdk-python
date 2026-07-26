"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventTriggerSummaryItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.tag_map
    import capo_customer_profiles.types.text
    import capo_customer_profiles.types.timestamp
    import capo_customer_profiles.types.type_name


class EventTriggerSummaryItem(TypedDict, closed=True):
    object_type_name: NotRequired["capo_customer_profiles.types.type_name.typeName"]
    """<p>The unique name of the object type.</p>"""
    event_trigger_name: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>The unique name of the event trigger.</p>"""
    description: NotRequired["capo_customer_profiles.types.text.text"]
    """<p>The description of the event trigger.</p>"""
    created_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the event trigger was created.</p>"""
    last_updated_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the event trigger was most recently updated.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
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
        import capo_customer_profiles.types.timestamp

        out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_customer_profiles.types.timestamp

        out["LastUpdatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
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
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "LastUpdatedAt" in data:
        import capo_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            capo_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    if "Tags" in data:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
