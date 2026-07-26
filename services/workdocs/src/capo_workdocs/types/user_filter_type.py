"""Generated from Smithy shape ``com.amazonaws.workdocs#UserFilterType``."""

from typing import Literal, TypeAlias, cast

UserFilterType: TypeAlias = Literal[
    "ALL",
    "ACTIVE_PENDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: UserFilterType) -> str:
    return value


def deserialize_json(data: str) -> UserFilterType:
    return cast(UserFilterType, data)
