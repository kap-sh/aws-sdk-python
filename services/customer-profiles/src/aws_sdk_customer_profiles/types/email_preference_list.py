"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EmailPreferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.contact_preference

EmailPreferenceList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.contact_preference.ContactPreference"
]


# --- restJson1 ser/de ---
def serialize_json(value: EmailPreferenceList) -> list:
    import aws_sdk_customer_profiles.types.contact_preference

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.contact_preference.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EmailPreferenceList:
    import aws_sdk_customer_profiles.types.contact_preference

    out: EmailPreferenceList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.contact_preference.deserialize_json(item)
        )
    return out
