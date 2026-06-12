"""Generated from Smithy shape ``com.amazonaws.chime#AccountStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime.errors import DeserializationError

AccountStatus: TypeAlias = Literal[
    "Suspended",
    "Active",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Suspended",
        "Active",
    )
)


def serialize_json(value: AccountStatus) -> str:
    return value


def deserialize_json(data: str) -> AccountStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccountStatus value: {data!r}")
    return cast(AccountStatus, data)
