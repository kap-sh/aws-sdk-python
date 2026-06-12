"""Generated from Smithy shape ``com.amazonaws.sesv2#CreateContactRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.attributes_data
    import aws_sdk_sesv2.types.contact_list_name
    import aws_sdk_sesv2.types.email_address
    import aws_sdk_sesv2.types.topic_preference_list
    import aws_sdk_sesv2.types.unsubscribe_all


class CreateContactRequest(TypedDict):
    contact_list_name: "aws_sdk_sesv2.types.contact_list_name.ContactListName"
    """<p>The name of the contact list to which the contact should be added.</p>"""
    email_address: "aws_sdk_sesv2.types.email_address.EmailAddress"
    """<p>The contact's email address.</p>"""
    topic_preferences: NotRequired[
        "aws_sdk_sesv2.types.topic_preference_list.TopicPreferenceList"
    ]
    """<p>The contact's preferences for being opted-in to or opted-out of topics.</p>"""
    unsubscribe_all: "aws_sdk_sesv2.types.unsubscribe_all.UnsubscribeAll"
    """<p>A boolean value status noting if the contact is unsubscribed from all contact list topics.</p>"""
    attributes_data: NotRequired["aws_sdk_sesv2.types.attributes_data.AttributesData"]
    """<p>The attribute data attached to a contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateContactRequest) -> dict:
    out: dict = {}
    out["EmailAddress"] = value["email_address"]
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


def deserialize_json(data: dict) -> CreateContactRequest:
    out: CreateContactRequest = {}  # type: ignore[typeddict-item]
    if "EmailAddress" in data:
        out["email_address"] = data["EmailAddress"]
    else:
        raise DeserializationError("CreateContactRequest.email_address required")
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
