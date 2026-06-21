"""Generated from Smithy shape ``com.amazonaws.wickr#UserStatus``."""

from typing import Literal, TypeAlias, cast

UserStatus: TypeAlias = Literal[
    1,
    2,
]


# --- restJson1 ser/de ---
def serialize_json(value: UserStatus) -> int:
    return value


def deserialize_json(data: int) -> UserStatus:
    return cast(UserStatus, data)
