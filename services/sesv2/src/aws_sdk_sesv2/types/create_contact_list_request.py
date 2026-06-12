"""Generated from Smithy shape ``com.amazonaws.sesv2#CreateContactListRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.contact_list_name
    import aws_sdk_sesv2.types.description
    import aws_sdk_sesv2.types.tag_list
    import aws_sdk_sesv2.types.topics


class CreateContactListRequest(TypedDict):
    contact_list_name: "aws_sdk_sesv2.types.contact_list_name.ContactListName"
    """<p>The name of the contact list.</p>"""
    topics: NotRequired["aws_sdk_sesv2.types.topics.Topics"]
    """<p>An interest group, theme, or label within a list. A contact list can have multiple topics.</p>"""
    description: NotRequired["aws_sdk_sesv2.types.description.Description"]
    """<p>A description of what the contact list is about.</p>"""
    tags: NotRequired["aws_sdk_sesv2.types.tag_list.TagList"]
    """<p>The tags associated with a contact list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateContactListRequest) -> dict:
    out: dict = {}
    out["ContactListName"] = value["contact_list_name"]
    if "topics" in value:
        import aws_sdk_sesv2.types.topics

        out["Topics"] = aws_sdk_sesv2.types.topics.serialize_json(value["topics"])
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import aws_sdk_sesv2.types.tag_list

        out["Tags"] = aws_sdk_sesv2.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateContactListRequest:
    out: CreateContactListRequest = {}  # type: ignore[typeddict-item]
    if "ContactListName" in data:
        out["contact_list_name"] = data["ContactListName"]
    else:
        raise DeserializationError(
            "CreateContactListRequest.contact_list_name required"
        )
    if "Topics" in data:
        import aws_sdk_sesv2.types.topics

        out["topics"] = aws_sdk_sesv2.types.topics.deserialize_json(data["Topics"])
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import aws_sdk_sesv2.types.tag_list

        out["tags"] = aws_sdk_sesv2.types.tag_list.deserialize_json(data["Tags"])
    return out
