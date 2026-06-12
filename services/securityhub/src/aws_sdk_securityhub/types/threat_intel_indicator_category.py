"""Generated from Smithy shape ``com.amazonaws.securityhub#ThreatIntelIndicatorCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

ThreatIntelIndicatorCategory: TypeAlias = Literal[
    "BACKDOOR",
    "CARD_STEALER",
    "COMMAND_AND_CONTROL",
    "DROP_SITE",
    "EXPLOIT_SITE",
    "KEYLOGGER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BACKDOOR",
        "CARD_STEALER",
        "COMMAND_AND_CONTROL",
        "DROP_SITE",
        "EXPLOIT_SITE",
        "KEYLOGGER",
    )
)


def serialize_json(value: ThreatIntelIndicatorCategory) -> str:
    return value


def deserialize_json(data: str) -> ThreatIntelIndicatorCategory:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ThreatIntelIndicatorCategory value: {data!r}"
        )
    return cast(ThreatIntelIndicatorCategory, data)
