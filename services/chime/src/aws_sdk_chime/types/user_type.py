"""Generated from Smithy shape ``com.amazonaws.chime#UserType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime.errors import DeserializationError

UserType: TypeAlias = Literal[
    "PrivateUser",
    "SharedDevice",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PrivateUser",
        "SharedDevice",
    )
)


def serialize_json(value: UserType) -> str:
    return value


def deserialize_json(data: str) -> UserType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserType value: {data!r}")
    return cast(UserType, data)
