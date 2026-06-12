"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlResponse``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

ControlResponse: TypeAlias = Literal[
    "MANUAL",
    "AUTOMATE",
    "DEFER",
    "IGNORE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MANUAL",
        "AUTOMATE",
        "DEFER",
        "IGNORE",
    )
)


def serialize_json(value: ControlResponse) -> str:
    return value


def deserialize_json(data: str) -> ControlResponse:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ControlResponse value: {data!r}")
    return cast(ControlResponse, data)
