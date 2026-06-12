"""Generated from Smithy shape ``com.amazonaws.sesv2#ListManagementOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.contact_list_name
    import aws_sdk_sesv2.types.topic_name


class ListManagementOptions(TypedDict):
    contact_list_name: "aws_sdk_sesv2.types.contact_list_name.ContactListName"
    """<p>The name of the contact list.</p>"""
    topic_name: NotRequired["aws_sdk_sesv2.types.topic_name.TopicName"]
    """<p>The name of the topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagementOptions) -> dict:
    out: dict = {}
    out["ContactListName"] = value["contact_list_name"]
    if "topic_name" in value:
        out["TopicName"] = value["topic_name"]
    return out


def deserialize_json(data: dict) -> ListManagementOptions:
    out: ListManagementOptions = {}  # type: ignore[typeddict-item]
    if "ContactListName" in data:
        out["contact_list_name"] = data["ContactListName"]
    else:
        raise DeserializationError("ListManagementOptions.contact_list_name required")
    if "TopicName" in data:
        out["topic_name"] = data["TopicName"]
    return out
