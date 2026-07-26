"""Generated from Smithy shape ``com.amazonaws.medialive#FollowPoint``."""

from typing import Literal, TypeAlias, cast

"""Follow reference point."""
FollowPoint: TypeAlias = Literal[
    "END",
    "START",
]


# --- restJson1 ser/de ---
def serialize_json(value: FollowPoint) -> str:
    return value


def deserialize_json(data: str) -> FollowPoint:
    return cast(FollowPoint, data)
