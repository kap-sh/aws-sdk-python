"""Generated from Smithy shape ``com.amazonaws.mediatailor#AdsInteractionPublishOptInEventType``."""

from typing import Literal, TypeAlias, cast

AdsInteractionPublishOptInEventType: TypeAlias = Literal[
    "RAW_ADS_RESPONSE",
    "RAW_ADS_REQUEST",
    "PRE_ADS_REQUEST_HOOK_SUMMARY",
    "PRE_ADS_REQUEST_FUNCTION_COMPLETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AdsInteractionPublishOptInEventType) -> str:
    return value


def deserialize_json(data: str) -> AdsInteractionPublishOptInEventType:
    return cast(AdsInteractionPublishOptInEventType, data)
