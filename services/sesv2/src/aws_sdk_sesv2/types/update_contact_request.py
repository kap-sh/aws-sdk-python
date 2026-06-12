"""Generated from Smithy shape ``com.amazonaws.sesv2#UpdateContactRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.attributes_data
    import aws_sdk_sesv2.types.contact_list_name
    import aws_sdk_sesv2.types.email_address
    import aws_sdk_sesv2.types.topic_preference_list
    import aws_sdk_sesv2.types.unsubscribe_all


class UpdateContactRequest(TypedDict):
    contact_list_name: "aws_sdk_sesv2.types.contact_list_name.ContactListName"
    """<p>The name of the contact list.</p>"""
    email_address: "aws_sdk_sesv2.types.email_address.EmailAddress"
    """<p>The contact's email address.</p>"""
    topic_preferences: NotRequired[
        "aws_sdk_sesv2.types.topic_preference_list.TopicPreferenceList"
    ]
    """<p>The contact's preference for being opted-in to or opted-out of a topic.</p>"""
    unsubscribe_all: "aws_sdk_sesv2.types.unsubscribe_all.UnsubscribeAll"
    """<p>A boolean value status noting if the contact is unsubscribed from all contact list topics.</p>"""
    attributes_data: NotRequired["aws_sdk_sesv2.types.attributes_data.AttributesData"]
    """<p>The attribute data attached to a contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateContactRequest) -> dict:
    out: dict = {}
    if "topic_preferences" in value:
        import aws_sdk_sesv2.types.topic_preference_list

        out["TopicPreferences"] = (
            aws_sdk_sesv2.types.topic_preference_list.serialize_json(
                value["topic_preferences"]
            )
        )
    out["UnsubscribeAll"] = value.get("unsubscribe_all", False)
    if "attributes_data" in value:
        out["AttributesData"] = value["attributes_data"]
    return out


def deserialize_json(data: dict) -> UpdateContactRequest:
    out: UpdateContactRequest = {}  # type: ignore[typeddict-item]
    if "TopicPreferences" in data:
        import aws_sdk_sesv2.types.topic_preference_list

        out["topic_preferences"] = (
            aws_sdk_sesv2.types.topic_preference_list.deserialize_json(
                data["TopicPreferences"]
            )
        )
    if "UnsubscribeAll" in data:
        out["unsubscribe_all"] = data["UnsubscribeAll"]
    else:
        out["unsubscribe_all"] = False
    if "AttributesData" in data:
        out["attributes_data"] = data["AttributesData"]
    return out
