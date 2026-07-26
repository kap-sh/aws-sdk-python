"""Generated from Smithy shape ``com.amazonaws.sesv2#GetContactListResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.contact_list_name
    import capo_sesv2.types.description
    import capo_sesv2.types.tag_list
    import capo_sesv2.types.timestamp
    import capo_sesv2.types.topics


class GetContactListResponse(TypedDict, closed=True):
    contact_list_name: NotRequired["capo_sesv2.types.contact_list_name.ContactListName"]
    """<p>The name of the contact list.</p>"""
    topics: NotRequired["capo_sesv2.types.topics.Topics"]
    """<p>An interest group, theme, or label within a list. A contact list can have multiple topics.</p>"""
    description: NotRequired["capo_sesv2.types.description.Description"]
    """<p>A description of what the contact list is about.</p>"""
    created_timestamp: NotRequired["capo_sesv2.types.timestamp.Timestamp"]
    """<p>A timestamp noting when the contact list was created.</p>"""
    last_updated_timestamp: NotRequired["capo_sesv2.types.timestamp.Timestamp"]
    """<p>A timestamp noting the last time the contact list was updated.</p>"""
    tags: NotRequired["capo_sesv2.types.tag_list.TagList"]
    """<p>The tags associated with a contact list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContactListResponse) -> dict:
    out: dict = {}
    if "contact_list_name" in value:
        out["ContactListName"] = value["contact_list_name"]
    if "topics" in value:
        import capo_sesv2.types.topics

        out["Topics"] = capo_sesv2.types.topics.serialize_json(value["topics"])
    if "description" in value:
        out["Description"] = value["description"]
    if "created_timestamp" in value:
        import capo_sesv2.types.timestamp

        out["CreatedTimestamp"] = capo_sesv2.types.timestamp.serialize_json(
            value["created_timestamp"]
        )
    if "last_updated_timestamp" in value:
        import capo_sesv2.types.timestamp

        out["LastUpdatedTimestamp"] = capo_sesv2.types.timestamp.serialize_json(
            value["last_updated_timestamp"]
        )
    if "tags" in value:
        import capo_sesv2.types.tag_list

        out["Tags"] = capo_sesv2.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetContactListResponse:
    out: GetContactListResponse = {}  # type: ignore[typeddict-item]
    if "ContactListName" in data:
        out["contact_list_name"] = data["ContactListName"]
    if "Topics" in data:
        import capo_sesv2.types.topics

        out["topics"] = capo_sesv2.types.topics.deserialize_json(data["Topics"])
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedTimestamp" in data:
        import capo_sesv2.types.timestamp

        out["created_timestamp"] = capo_sesv2.types.timestamp.deserialize_json(
            data["CreatedTimestamp"]
        )
    if "LastUpdatedTimestamp" in data:
        import capo_sesv2.types.timestamp

        out["last_updated_timestamp"] = capo_sesv2.types.timestamp.deserialize_json(
            data["LastUpdatedTimestamp"]
        )
    if "Tags" in data:
        import capo_sesv2.types.tag_list

        out["tags"] = capo_sesv2.types.tag_list.deserialize_json(data["Tags"])
    return out
