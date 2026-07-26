"""Generated from Smithy shape ``com.amazonaws.datazone#UserSearchType``."""

from typing import Literal, TypeAlias, cast

UserSearchType: TypeAlias = Literal[
    "SSO_USER",
    "DATAZONE_USER",
    "DATAZONE_SSO_USER",
    "DATAZONE_IAM_USER",
]


# --- restJson1 ser/de ---
def serialize_json(value: UserSearchType) -> str:
    return value


def deserialize_json(data: str) -> UserSearchType:
    return cast(UserSearchType, data)
