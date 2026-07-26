"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#EndpointErrorCondition``."""

from typing import Literal, TypeAlias, cast

EndpointErrorCondition: TypeAlias = Literal[
    "STALE_MANIFEST",
    "INCOMPLETE_MANIFEST",
    "MISSING_DRM_KEY",
    "SLATE_INPUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointErrorCondition) -> str:
    return value


def deserialize_json(data: str) -> EndpointErrorCondition:
    return cast(EndpointErrorCondition, data)
