"""Generated from Smithy shape ``com.amazonaws.pinpointemail#IdentityType``."""

from typing import Literal, TypeAlias, cast

"""<p>The email identity type. The identity type can be one of the following:</p> <ul> <li> <p> <code>EMAIL_ADDRESS</code> – The identity is an email address.</p> </li> <li> <p> <code>DOMAIN</code> – The identity is a domain.</p> </li> </ul>"""
IdentityType: TypeAlias = Literal[
    "EMAIL_ADDRESS",
    "DOMAIN",
    "MANAGED_DOMAIN",
]


# --- restJson1 ser/de ---
def serialize_json(value: IdentityType) -> str:
    return value


def deserialize_json(data: str) -> IdentityType:
    return cast(IdentityType, data)
