"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ContactType``."""

from typing import Literal, TypeAlias, cast

ContactType: TypeAlias = Literal[
    "PhoneNumber",
    "MobilePhoneNumber",
    "HomePhoneNumber",
    "BusinessPhoneNumber",
    "EmailAddress",
    "PersonalEmailAddress",
    "BusinessEmailAddress",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactType) -> str:
    return value


def deserialize_json(data: str) -> ContactType:
    return cast(ContactType, data)
