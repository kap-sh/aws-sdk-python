"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ProfileOwnerType``."""

from typing import Literal, TypeAlias, cast

ProfileOwnerType: TypeAlias = Literal[
    "SELF",
    "SHARED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileOwnerType) -> str:
    return value


def deserialize_json(data: str) -> ProfileOwnerType:
    return cast(ProfileOwnerType, data)
