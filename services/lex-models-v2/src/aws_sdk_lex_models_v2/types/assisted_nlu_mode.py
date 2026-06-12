"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AssistedNluMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

"""<p>Defines the operational mode for Assisted Natural Language Understanding. This enum determines how the enhanced NLU capabilities integrate with standard intent recognition.</p>"""
AssistedNluMode: TypeAlias = Literal[
    "Primary",
    "Fallback",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Primary",
        "Fallback",
    )
)


def serialize_json(value: AssistedNluMode) -> str:
    return value


def deserialize_json(data: str) -> AssistedNluMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssistedNluMode value: {data!r}")
    return cast(AssistedNluMode, data)
