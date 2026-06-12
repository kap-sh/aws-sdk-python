"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ProfileNotificationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

ProfileNotificationType: TypeAlias = Literal[
    "PROFILE_ANSWERS_UPDATED",
    "PROFILE_DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROFILE_ANSWERS_UPDATED",
        "PROFILE_DELETED",
    )
)


def serialize_json(value: ProfileNotificationType) -> str:
    return value


def deserialize_json(data: str) -> ProfileNotificationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProfileNotificationType value: {data!r}")
    return cast(ProfileNotificationType, data)
