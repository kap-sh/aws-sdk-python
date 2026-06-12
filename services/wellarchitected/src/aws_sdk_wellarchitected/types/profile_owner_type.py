"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ProfileOwnerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

ProfileOwnerType: TypeAlias = Literal[
    "SELF",
    "SHARED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SELF",
        "SHARED",
    )
)


def serialize_json(value: ProfileOwnerType) -> str:
    return value


def deserialize_json(data: str) -> ProfileOwnerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProfileOwnerType value: {data!r}")
    return cast(ProfileOwnerType, data)
