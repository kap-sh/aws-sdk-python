"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ScteFilter``."""

from typing import Literal, TypeAlias, cast

ScteFilter: TypeAlias = Literal[
    "SPLICE_INSERT",
    "BREAK",
    "PROVIDER_ADVERTISEMENT",
    "DISTRIBUTOR_ADVERTISEMENT",
    "PROVIDER_PLACEMENT_OPPORTUNITY",
    "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
    "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
    "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
    "PROGRAM",
    "CHAPTER",
    "UNSCHEDULED_EVENT",
    "ALTERNATE_CONTENT_OPPORTUNITY",
    "NETWORK",
    "PROVIDER_PROMO",
    "DISTRIBUTOR_PROMO",
    "PROVIDER_AD_BLOCK",
    "DISTRIBUTOR_AD_BLOCK",
    "CONTENT_IDENTIFICATION",
    "CALL_AD_SERVER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScteFilter) -> str:
    return value


def deserialize_json(data: str) -> ScteFilter:
    return cast(ScteFilter, data)
