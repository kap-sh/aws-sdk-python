"""Generated from Smithy shape ``com.amazonaws.eks#SsoIdentityType``."""

from typing import Literal, TypeAlias, cast

SsoIdentityType: TypeAlias = Literal[
    "SSO_USER",
    "SSO_GROUP",
]


# --- restJson1 ser/de ---
def serialize_json(value: SsoIdentityType) -> str:
    return value


def deserialize_json(data: str) -> SsoIdentityType:
    return cast(SsoIdentityType, data)
