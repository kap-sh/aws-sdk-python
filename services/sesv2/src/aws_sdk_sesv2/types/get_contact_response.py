"""Generated from Smithy shape ``com.amazonaws.sesv2#GetContactResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.attributes_data
    import aws_sdk_sesv2.types.contact_list_name
    import aws_sdk_sesv2.types.email_address
    import aws_sdk_sesv2.types.timestamp
    import aws_sdk_sesv2.types.topic_preference_list
    import aws_sdk_sesv2.types.unsubscribe_all


class GetContactResponse(TypedDict):
    contact_list_name: NotRequired[
        "aws_sdk_sesv2.types.contact_list_name.ContactListName"
    ]
    """<p>The name of the contact list to which the contact belongs.</p>"""
    email_address: NotRequired["aws_sdk_sesv2.types.email_address.EmailAddress"]
    """<p>The contact's email address.</p>"""
    topic_preferences: NotRequired[
        "aws_sdk_sesv2.types.topic_preference_list.TopicPreferenceList"
    ]
    """<p>The contact's preference for being opted-in to or opted-out of a topic.></p>"""
    topic_default_preferences: NotRequired[
        "aws_sdk_sesv2.types.topic_preference_list.TopicPreferenceList"
    ]
    """<p>The default topic preferences applied to the contact.</p>"""
    unsubscribe_all: "aws_sdk_sesv2.types.unsubscribe_all.UnsubscribeAll"
    """<p>A boolean value status noting if the contact is unsubscribed from all contact list topics.</p>"""
    attributes_data: NotRequired["aws_sdk_sesv2.types.attributes_data.AttributesData"]
    """<p>The attribute data attached to a contact.</p>"""
    created_timestamp: NotRequired["aws_sdk_sesv2.types.timestamp.Timestamp"]
    """<p>A timestamp noting when the contact was created.</p>"""
    last_updated_timestamp: NotRequired["aws_sdk_sesv2.types.timestamp.Timestamp"]
    """<p>A timestamp noting the last time the contact's information was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContactResponse) -> dict:
    out: dict = {}
    if "contact_list_name" in value:
        out["ContactListName"] = value["contact_list_name"]
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    if "topic_preferences" in value:
        import aws_sdk_sesv2.types.topic_preference_list

        out["TopicPreferences"] = (
            aws_sdk_sesv2.types.topic_preference_list.serialize_json(
                value["topic_preferences"]
            )
        )
    if "topic_default_preferences" in value:
        import aws_sdk_sesv2.types.topic_preference_list

        out["TopicDefaultPreferences"] = (
            aws_sdk_sesv2.types.topic_preference_list.serialize_json(
                value["topic_default_preferences"]
            )
        )
    out["UnsubscribeAll"] = value.get("unsubscribe_all", False)
    if "attributes_data" in value:
        out["AttributesData"] = value["attributes_data"]
    if "created_timestamp" in value:
        import aws_sdk_sesv2.types.timestamp

        out["CreatedTimestamp"] = aws_sdk_sesv2.types.timestamp.serialize_json(
            value["created_timestamp"]
        )
    if "last_updated_timestamp" in value:
        import aws_sdk_sesv2.types.timestamp

        out["LastUpdatedTimestamp"] = aws_sdk_sesv2.types.timestamp.serialize_json(
            value["last_updated_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> GetContactResponse:
    out: GetContactResponse = {}  # type: ignore[typeddict-item]
    if "ContactListName" in data:
        out["contact_list_name"] = data["ContactListName"]
    if "EmailAddress" in data:
        out["email_address"] = data["EmailAddress"]
    if "TopicPreferences" in data:
        import aws_sdk_sesv2.types.topic_preference_list

        out["topic_preferences"] = (
            aws_sdk_sesv2.types.topic_preference_list.deserialize_json(
                data["TopicPreferences"]
            )
        )
    if "TopicDefaultPreferences" in data:
        import aws_sdk_sesv2.types.topic_preference_list

        out["topic_default_preferences"] = (
            aws_sdk_sesv2.types.topic_preference_list.deserialize_json(
                data["TopicDefaultPreferences"]
            )
        )
    if "UnsubscribeAll" in data:
        out["unsubscribe_all"] = data["UnsubscribeAll"]
    else:
        out["unsubscribe_all"] = False
    if "AttributesData" in data:
        out["attributes_data"] = data["AttributesData"]
    if "CreatedTimestamp" in data:
        import aws_sdk_sesv2.types.timestamp

        out["created_timestamp"] = aws_sdk_sesv2.types.timestamp.deserialize_json(
            data["CreatedTimestamp"]
        )
    if "LastUpdatedTimestamp" in data:
        import aws_sdk_sesv2.types.timestamp

        out["last_updated_timestamp"] = aws_sdk_sesv2.types.timestamp.deserialize_json(
            data["LastUpdatedTimestamp"]
        )
    return out
