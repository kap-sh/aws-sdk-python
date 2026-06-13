"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#EndpointErrorCondition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

EndpointErrorCondition: TypeAlias = Literal[
    "STALE_MANIFEST",
    "INCOMPLETE_MANIFEST",
    "MISSING_DRM_KEY",
    "SLATE_INPUT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STALE_MANIFEST",
        "INCOMPLETE_MANIFEST",
        "MISSING_DRM_KEY",
        "SLATE_INPUT",
    )
)


def serialize_json(value: EndpointErrorCondition) -> str:
    return value


def deserialize_json(data: str) -> EndpointErrorCondition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EndpointErrorCondition value: {data!r}")
    return cast(EndpointErrorCondition, data)
