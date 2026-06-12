"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#GenerationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

GenerationStatus: TypeAlias = Literal[
    "Failed",
    "Complete",
    "InProgress",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Failed",
        "Complete",
        "InProgress",
    )
)


def serialize_json(value: GenerationStatus) -> str:
    return value


def deserialize_json(data: str) -> GenerationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GenerationStatus value: {data!r}")
    return cast(GenerationStatus, data)
