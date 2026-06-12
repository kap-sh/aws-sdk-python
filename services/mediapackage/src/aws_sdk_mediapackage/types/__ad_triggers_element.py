"""Generated from Smithy shape ``com.amazonaws.mediapackage#__AdTriggersElement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackage.errors import DeserializationError

__AdTriggersElement: TypeAlias = Literal[
    "SPLICE_INSERT",
    "BREAK",
    "PROVIDER_ADVERTISEMENT",
    "DISTRIBUTOR_ADVERTISEMENT",
    "PROVIDER_PLACEMENT_OPPORTUNITY",
    "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
    "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
    "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
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
    )
)


def serialize_json(value: __AdTriggersElement) -> str:
    return value


def deserialize_json(data: str) -> __AdTriggersElement:
    if data not in _VALUES:
        raise DeserializationError(f"unknown __AdTriggersElement value: {data!r}")
    return cast(__AdTriggersElement, data)
