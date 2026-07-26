"""Generated from Smithy shape ``com.amazonaws.sesv2#UpdateContactListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.contact_list_name
    import capo_sesv2.types.description
    import capo_sesv2.types.topics


class UpdateContactListRequest(TypedDict, closed=True):
    contact_list_name: "capo_sesv2.types.contact_list_name.ContactListName"
    """<p>The name of the contact list.</p>"""
    topics: NotRequired["capo_sesv2.types.topics.Topics"]
    """<p>An interest group, theme, or label within a list. A contact list can have multiple topics.</p>"""
    description: NotRequired["capo_sesv2.types.description.Description"]
    """<p>A description of what the contact list is about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateContactListRequest) -> dict:
    out: dict = {}
    if "topics" in value:
        import capo_sesv2.types.topics

        out["Topics"] = capo_sesv2.types.topics.serialize_json(value["topics"])
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateContactListRequest:
    out: UpdateContactListRequest = {}  # type: ignore[typeddict-item]
    if "Topics" in data:
        import capo_sesv2.types.topics

        out["topics"] = capo_sesv2.types.topics.deserialize_json(data["Topics"])
    if "Description" in data:
        out["description"] = data["Description"]
    return out
