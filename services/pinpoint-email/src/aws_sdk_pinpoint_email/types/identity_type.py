"""Generated from Smithy shape ``com.amazonaws.pinpointemail#IdentityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint_email.errors import DeserializationError

"""<p>The email identity type. The identity type can be one of the following:</p> <ul> <li> <p> <code>EMAIL_ADDRESS</code> – The identity is an email address.</p> </li> <li> <p> <code>DOMAIN</code> – The identity is a domain.</p> </li> </ul>"""
IdentityType: TypeAlias = Literal[
    "EMAIL_ADDRESS",
    "DOMAIN",
    "MANAGED_DOMAIN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EMAIL_ADDRESS",
        "DOMAIN",
        "MANAGED_DOMAIN",
    )
)


def serialize_json(value: IdentityType) -> str:
    return value


def deserialize_json(data: str) -> IdentityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IdentityType value: {data!r}")
    return cast(IdentityType, data)
