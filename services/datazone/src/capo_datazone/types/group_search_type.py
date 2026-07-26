"""Generated from Smithy shape ``com.amazonaws.datazone#GroupSearchType``."""

from typing import Literal, TypeAlias, cast

GroupSearchType: TypeAlias = Literal[
    "SSO_GROUP",
    "DATAZONE_SSO_GROUP",
    "IAM_ROLE_SESSION_GROUP",
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupSearchType) -> str:
    return value


def deserialize_json(data: str) -> GroupSearchType:
    return cast(GroupSearchType, data)
