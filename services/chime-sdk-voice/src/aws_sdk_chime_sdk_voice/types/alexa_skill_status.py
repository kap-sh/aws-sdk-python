"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#AlexaSkillStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_voice.errors import DeserializationError

AlexaSkillStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_json(value: AlexaSkillStatus) -> str:
    return value


def deserialize_json(data: str) -> AlexaSkillStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AlexaSkillStatus value: {data!r}")
    return cast(AlexaSkillStatus, data)
