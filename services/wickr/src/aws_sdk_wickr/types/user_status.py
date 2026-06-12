"""Generated from Smithy shape ``com.amazonaws.wickr#UserStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wickr.errors import DeserializationError

UserStatus: TypeAlias = Literal[
    1,
    2,
]


# --- restJson1 ser/de ---
_VALUES: frozenset[int] = frozenset(
    (
        1,
        2,
    )
)


def serialize_json(value: UserStatus) -> int:
    return value


def deserialize_json(data: int) -> UserStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserStatus value: {data!r}")
    return cast(UserStatus, data)
