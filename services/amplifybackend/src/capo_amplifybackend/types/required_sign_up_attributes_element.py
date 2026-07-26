"""Generated from Smithy shape ``com.amazonaws.amplifybackend#RequiredSignUpAttributesElement``."""

from typing import Literal, TypeAlias, cast

RequiredSignUpAttributesElement: TypeAlias = Literal[
    "ADDRESS",
    "BIRTHDATE",
    "EMAIL",
    "FAMILY_NAME",
    "GENDER",
    "GIVEN_NAME",
    "LOCALE",
    "MIDDLE_NAME",
    "NAME",
    "NICKNAME",
    "PHONE_NUMBER",
    "PICTURE",
    "PREFERRED_USERNAME",
    "PROFILE",
    "UPDATED_AT",
    "WEBSITE",
    "ZONE_INFO",
]


# --- restJson1 ser/de ---
def serialize_json(value: RequiredSignUpAttributesElement) -> str:
    return value


def deserialize_json(data: str) -> RequiredSignUpAttributesElement:
    return cast(RequiredSignUpAttributesElement, data)
