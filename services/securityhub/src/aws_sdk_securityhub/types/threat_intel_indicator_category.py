"""Generated from Smithy shape ``com.amazonaws.securityhub#ThreatIntelIndicatorCategory``."""

from typing import Literal, TypeAlias, cast

ThreatIntelIndicatorCategory: TypeAlias = Literal[
    "BACKDOOR",
    "CARD_STEALER",
    "COMMAND_AND_CONTROL",
    "DROP_SITE",
    "EXPLOIT_SITE",
    "KEYLOGGER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatIntelIndicatorCategory) -> str:
    return value


def deserialize_json(data: str) -> ThreatIntelIndicatorCategory:
    return cast(ThreatIntelIndicatorCategory, data)
