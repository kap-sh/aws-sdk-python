"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EngagementPreferences``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.email_preference_list
    import capo_customer_profiles.types.phone_preference_list


class EngagementPreferences(TypedDict, closed=True):
    phone: NotRequired[
        "capo_customer_profiles.types.phone_preference_list.PhonePreferenceList"
    ]
    """<p>A list of phone-related contact preferences</p>"""
    email: NotRequired[
        "capo_customer_profiles.types.email_preference_list.EmailPreferenceList"
    ]
    """<p>A list of email-related contact preferences</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EngagementPreferences) -> dict:
    out: dict = {}
    if "phone" in value:
        import capo_customer_profiles.types.phone_preference_list

        out["Phone"] = (
            capo_customer_profiles.types.phone_preference_list.serialize_json(
                value["phone"]
            )
        )
    if "email" in value:
        import capo_customer_profiles.types.email_preference_list

        out["Email"] = (
            capo_customer_profiles.types.email_preference_list.serialize_json(
                value["email"]
            )
        )
    return out


def deserialize_json(data: dict) -> EngagementPreferences:
    out: EngagementPreferences = {}  # type: ignore[typeddict-item]
    if "Phone" in data:
        import capo_customer_profiles.types.phone_preference_list

        out["phone"] = (
            capo_customer_profiles.types.phone_preference_list.deserialize_json(
                data["Phone"]
            )
        )
    if "Email" in data:
        import capo_customer_profiles.types.email_preference_list

        out["email"] = (
            capo_customer_profiles.types.email_preference_list.deserialize_json(
                data["Email"]
            )
        )
    return out
