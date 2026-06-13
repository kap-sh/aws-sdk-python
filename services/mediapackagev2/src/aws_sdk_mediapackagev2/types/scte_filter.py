"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ScteFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: ScteFilter) -> str:
    return value


def deserialize_json(data: str) -> ScteFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScteFilter value: {data!r}")
    return cast(ScteFilter, data)
