"""Generated from Smithy shape ``com.amazonaws.networkmanager#ChangeAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

ChangeAction: TypeAlias = Literal[
    "ADD",
    "MODIFY",
    "REMOVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ADD",
        "MODIFY",
        "REMOVE",
    )
)


def serialize_json(value: ChangeAction) -> str:
    return value


def deserialize_json(data: str) -> ChangeAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChangeAction value: {data!r}")
    return cast(ChangeAction, data)
