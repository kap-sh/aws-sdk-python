"""Generated from Smithy shape ``com.amazonaws.devopsagent#UserType``."""

from typing import Literal, TypeAlias, cast

"""<p>Types of users in the system</p>"""
UserType: TypeAlias = Literal[
    "IAM",
    "IDC",
    "IDP",
]


# --- restJson1 ser/de ---
def serialize_json(value: UserType) -> str:
    return value


def deserialize_json(data: str) -> UserType:
    return cast(UserType, data)
