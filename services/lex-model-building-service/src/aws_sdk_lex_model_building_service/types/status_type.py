"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#StatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_model_building_service.errors import DeserializationError

StatusType: TypeAlias = Literal[
    "Detected",
    "Missed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Detected",
        "Missed",
    )
)


def serialize_json(value: StatusType) -> str:
    return value


def deserialize_json(data: str) -> StatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StatusType value: {data!r}")
    return cast(StatusType, data)
