"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ContactType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "PhoneNumber",
        "MobilePhoneNumber",
        "HomePhoneNumber",
        "BusinessPhoneNumber",
        "EmailAddress",
        "PersonalEmailAddress",
        "BusinessEmailAddress",
    )
)


def serialize_json(value: ContactType) -> str:
    return value


def deserialize_json(data: str) -> ContactType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContactType value: {data!r}")
    return cast(ContactType, data)
