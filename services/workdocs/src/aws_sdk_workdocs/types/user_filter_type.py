"""Generated from Smithy shape ``com.amazonaws.workdocs#UserFilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

UserFilterType: TypeAlias = Literal[
    "ALL",
    "ACTIVE_PENDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "ACTIVE_PENDING",
    )
)


def serialize_json(value: UserFilterType) -> str:
    return value


def deserialize_json(data: str) -> UserFilterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserFilterType value: {data!r}")
    return cast(UserFilterType, data)
