"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ChangeRequestAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

ChangeRequestAction: TypeAlias = Literal[
    "APPROVE",
    "DENY",
    "CANCEL",
    "COMMIT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APPROVE",
        "DENY",
        "CANCEL",
        "COMMIT",
    )
)


def serialize_json(value: ChangeRequestAction) -> str:
    return value


def deserialize_json(data: str) -> ChangeRequestAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChangeRequestAction value: {data!r}")
    return cast(ChangeRequestAction, data)
