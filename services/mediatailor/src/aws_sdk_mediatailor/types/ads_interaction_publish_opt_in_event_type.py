"""Generated from Smithy shape ``com.amazonaws.mediatailor#AdsInteractionPublishOptInEventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediatailor.errors import DeserializationError

AdsInteractionPublishOptInEventType: TypeAlias = Literal[
    "RAW_ADS_RESPONSE",
    "RAW_ADS_REQUEST",
    "PRE_ADS_REQUEST_HOOK_SUMMARY",
    "PRE_ADS_REQUEST_FUNCTION_COMPLETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RAW_ADS_RESPONSE",
        "RAW_ADS_REQUEST",
        "PRE_ADS_REQUEST_HOOK_SUMMARY",
        "PRE_ADS_REQUEST_FUNCTION_COMPLETED",
    )
)


def serialize_json(value: AdsInteractionPublishOptInEventType) -> str:
    return value


def deserialize_json(data: str) -> AdsInteractionPublishOptInEventType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AdsInteractionPublishOptInEventType value: {data!r}"
        )
    return cast(AdsInteractionPublishOptInEventType, data)
