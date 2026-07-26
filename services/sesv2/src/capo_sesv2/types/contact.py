"""Generated from Smithy shape ``com.amazonaws.sesv2#Contact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.email_address
    import capo_sesv2.types.timestamp
    import capo_sesv2.types.topic_preference_list
    import capo_sesv2.types.unsubscribe_all


class Contact(TypedDict, closed=True):
    email_address: NotRequired["capo_sesv2.types.email_address.EmailAddress"]
    """<p>The contact's email address.</p>"""
    topic_preferences: NotRequired[
        "capo_sesv2.types.topic_preference_list.TopicPreferenceList"
    ]
    """<p>The contact's preference for being opted-in to or opted-out of a topic.</p>"""
    topic_default_preferences: NotRequired[
        "capo_sesv2.types.topic_preference_list.TopicPreferenceList"
    ]
    """<p>The default topic preferences applied to the contact.</p>"""
    unsubscribe_all: "capo_sesv2.types.unsubscribe_all.UnsubscribeAll"
    """<p>A boolean value status noting if the contact is unsubscribed from all contact list topics.</p>"""
    last_updated_timestamp: NotRequired["capo_sesv2.types.timestamp.Timestamp"]
    """<p>A timestamp noting the last time the contact's information was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Contact) -> dict:
    out: dict = {}
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    if "topic_preferences" in value:
        import capo_sesv2.types.topic_preference_list

        out["TopicPreferences"] = capo_sesv2.types.topic_preference_list.serialize_json(
            value["topic_preferences"]
        )
    if "topic_default_preferences" in value:
        import capo_sesv2.types.topic_preference_list

        out["TopicDefaultPreferences"] = (
            capo_sesv2.types.topic_preference_list.serialize_json(
                value["topic_default_preferences"]
            )
        )
    out["UnsubscribeAll"] = value.get("unsubscribe_all", False)
    if "last_updated_timestamp" in value:
        import capo_sesv2.types.timestamp

        out["LastUpdatedTimestamp"] = capo_sesv2.types.timestamp.serialize_json(
            value["last_updated_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> Contact:
    out: Contact = {}  # type: ignore[typeddict-item]
    if "EmailAddress" in data:
        out["email_address"] = data["EmailAddress"]
    if "TopicPreferences" in data:
        import capo_sesv2.types.topic_preference_list

        out["topic_preferences"] = (
            capo_sesv2.types.topic_preference_list.deserialize_json(
                data["TopicPreferences"]
            )
        )
    if "TopicDefaultPreferences" in data:
        import capo_sesv2.types.topic_preference_list

        out["topic_default_preferences"] = (
            capo_sesv2.types.topic_preference_list.deserialize_json(
                data["TopicDefaultPreferences"]
            )
        )
    if "UnsubscribeAll" in data:
        out["unsubscribe_all"] = data["UnsubscribeAll"]
    else:
        out["unsubscribe_all"] = False
    if "LastUpdatedTimestamp" in data:
        import capo_sesv2.types.timestamp

        out["last_updated_timestamp"] = capo_sesv2.types.timestamp.deserialize_json(
            data["LastUpdatedTimestamp"]
        )
    return out
