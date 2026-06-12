"""Generated from Smithy shape ``com.amazonaws.amplifybackend#RequiredSignUpAttributesElement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplifybackend.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: RequiredSignUpAttributesElement) -> str:
    return value


def deserialize_json(data: str) -> RequiredSignUpAttributesElement:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RequiredSignUpAttributesElement value: {data!r}"
        )
    return cast(RequiredSignUpAttributesElement, data)
