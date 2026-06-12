"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsModality``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AnalyticsModality: TypeAlias = Literal[
    "Speech",
    "Text",
    "DTMF",
    "MultiMode",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Speech",
        "Text",
        "DTMF",
        "MultiMode",
    )
)


def serialize_json(value: AnalyticsModality) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsModality:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalyticsModality value: {data!r}")
    return cast(AnalyticsModality, data)
