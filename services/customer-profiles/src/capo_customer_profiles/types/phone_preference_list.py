"""Generated from Smithy shape ``com.amazonaws.customerprofiles#PhonePreferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.contact_preference

PhonePreferenceList: TypeAlias = list[
    "capo_customer_profiles.types.contact_preference.ContactPreference"
]


# --- restJson1 ser/de ---
def serialize_json(value: PhonePreferenceList) -> list:
    import capo_customer_profiles.types.contact_preference

    out: list = []
    for item in value:
        out.append(capo_customer_profiles.types.contact_preference.serialize_json(item))
    return out


def deserialize_json(data: list) -> PhonePreferenceList:
    import capo_customer_profiles.types.contact_preference

    out: PhonePreferenceList = []
    for item in data:
        out.append(
            capo_customer_profiles.types.contact_preference.deserialize_json(item)
        )
    return out
