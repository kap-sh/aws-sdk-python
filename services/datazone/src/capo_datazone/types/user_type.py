"""Generated from Smithy shape ``com.amazonaws.datazone#UserType``."""

from typing import Literal, TypeAlias, cast

UserType: TypeAlias = Literal[
    "IAM_USER",
    "IAM_ROLE",
    "SSO_USER",
    "IAM_ROLE_SESSION",
]


# --- restJson1 ser/de ---
def serialize_json(value: UserType) -> str:
    return value


def deserialize_json(data: str) -> UserType:
    return cast(UserType, data)
