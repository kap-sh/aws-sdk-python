"""Generated from Smithy shape ``com.amazonaws.medialive#FollowPoint``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Follow reference point."""
FollowPoint: TypeAlias = Literal[
    "END",
    "START",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "END",
        "START",
    )
)


def serialize_json(value: FollowPoint) -> str:
    return value


def deserialize_json(data: str) -> FollowPoint:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FollowPoint value: {data!r}")
    return cast(FollowPoint, data)
