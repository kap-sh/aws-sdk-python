"""Generated from Smithy shape ``com.amazonaws.mediapackage#__AdTriggersElement``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: __AdTriggersElement) -> str:
    return value


def deserialize_json(data: str) -> __AdTriggersElement:
    return cast(__AdTriggersElement, data)
