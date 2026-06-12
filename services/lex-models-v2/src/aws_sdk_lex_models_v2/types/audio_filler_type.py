"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AudioFillerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

"""<p>The audio filler identifier played during speech-to-speech interactions. Supported values include melody and typing variants such as <code>MELODY_CHIPPER_CHIME</code>, <code>MELODY_CURIOUS_CRAWL</code>, <code>MELODY_RISING_RIPPLE</code>, <code>MELODY_PATIENT_PING</code>, <code>MELODY_PONDERING_PONG</code>, <code>TYPING_KINETIC_KEYS</code>, and <code>TYPING_QUIET_QWERTY</code>.</p>"""
AudioFillerType: TypeAlias = Literal[
    "MELODY_CHIPPER_CHIME",
    "MELODY_CURIOUS_CRAWL",
    "MELODY_RISING_RIPPLE",
    "MELODY_PATIENT_PING",
    "MELODY_PONDERING_PONG",
    "TYPING_KINETIC_KEYS",
    "TYPING_QUIET_QWERTY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MELODY_CHIPPER_CHIME",
        "MELODY_CURIOUS_CRAWL",
        "MELODY_RISING_RIPPLE",
        "MELODY_PATIENT_PING",
        "MELODY_PONDERING_PONG",
        "TYPING_KINETIC_KEYS",
        "TYPING_QUIET_QWERTY",
    )
)


def serialize_json(value: AudioFillerType) -> str:
    return value


def deserialize_json(data: str) -> AudioFillerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AudioFillerType value: {data!r}")
    return cast(AudioFillerType, data)
