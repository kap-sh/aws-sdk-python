"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#ProcessBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_model_building_service.errors import DeserializationError

ProcessBehavior: TypeAlias = Literal[
    "SAVE",
    "BUILD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SAVE",
        "BUILD",
    )
)


def serialize_json(value: ProcessBehavior) -> str:
    return value


def deserialize_json(data: str) -> ProcessBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProcessBehavior value: {data!r}")
    return cast(ProcessBehavior, data)
