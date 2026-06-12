"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#Status``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_model_building_service.errors import DeserializationError

Status: TypeAlias = Literal[
    "BUILDING",
    "READY",
    "READY_BASIC_TESTING",
    "FAILED",
    "NOT_BUILT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BUILDING",
        "READY",
        "READY_BASIC_TESTING",
        "FAILED",
        "NOT_BUILT",
    )
)


def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Status value: {data!r}")
    return cast(Status, data)
