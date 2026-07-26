"""Generated from Smithy shape ``com.amazonaws.datazone#UserProfileType``."""

from typing import Literal, TypeAlias, cast

UserProfileType: TypeAlias = Literal[
    "IAM",
    "SSO",
]


# --- restJson1 ser/de ---
def serialize_json(value: UserProfileType) -> str:
    return value


def deserialize_json(data: str) -> UserProfileType:
    return cast(UserProfileType, data)
