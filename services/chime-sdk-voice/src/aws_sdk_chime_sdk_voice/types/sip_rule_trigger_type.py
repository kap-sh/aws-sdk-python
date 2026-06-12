"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SipRuleTriggerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_voice.errors import DeserializationError

SipRuleTriggerType: TypeAlias = Literal[
    "ToPhoneNumber",
    "RequestUriHostname",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ToPhoneNumber",
        "RequestUriHostname",
    )
)


def serialize_json(value: SipRuleTriggerType) -> str:
    return value


def deserialize_json(data: str) -> SipRuleTriggerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SipRuleTriggerType value: {data!r}")
    return cast(SipRuleTriggerType, data)
