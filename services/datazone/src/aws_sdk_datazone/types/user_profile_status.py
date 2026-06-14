"""Generated from Smithy shape ``com.amazonaws.datazone#UserProfileStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

UserProfileStatus: TypeAlias = Literal[
    "ASSIGNED",
    "NOT_ASSIGNED",
    "ACTIVATED",
    "DEACTIVATED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSIGNED",
        "NOT_ASSIGNED",
        "ACTIVATED",
        "DEACTIVATED",
    )
)


def serialize_json(value: UserProfileStatus) -> str:
    return value


def deserialize_json(data: str) -> UserProfileStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserProfileStatus value: {data!r}")
    return cast(UserProfileStatus, data)
