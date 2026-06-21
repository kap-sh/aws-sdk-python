"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ProfileType``."""

from typing import Literal, TypeAlias, cast

ProfileType: TypeAlias = Literal[
    "ACCOUNT_PROFILE",
    "PROFILE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileType) -> str:
    return value


def deserialize_json(data: str) -> ProfileType:
    return cast(ProfileType, data)
