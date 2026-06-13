"""Generated from Smithy shape ``com.amazonaws.repostspace#Role``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_repostspace.errors import DeserializationError

Role: TypeAlias = Literal[
    "EXPERT",
    "MODERATOR",
    "ADMINISTRATOR",
    "SUPPORTREQUESTOR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXPERT",
        "MODERATOR",
        "ADMINISTRATOR",
        "SUPPORTREQUESTOR",
    )
)


def serialize_json(value: Role) -> str:
    return value


def deserialize_json(data: str) -> Role:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Role value: {data!r}")
    return cast(Role, data)
