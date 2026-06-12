"""Generated from Smithy shape ``com.amazonaws.workdocs#UserStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

UserStatusType: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "PENDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
        "PENDING",
    )
)


def serialize_json(value: UserStatusType) -> str:
    return value


def deserialize_json(data: str) -> UserStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserStatusType value: {data!r}")
    return cast(UserStatusType, data)
