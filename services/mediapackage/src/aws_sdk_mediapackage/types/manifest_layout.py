"""Generated from Smithy shape ``com.amazonaws.mediapackage#ManifestLayout``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackage.errors import DeserializationError

ManifestLayout: TypeAlias = Literal[
    "FULL",
    "COMPACT",
    "DRM_TOP_LEVEL_COMPACT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FULL",
        "COMPACT",
        "DRM_TOP_LEVEL_COMPACT",
    )
)


def serialize_json(value: ManifestLayout) -> str:
    return value


def deserialize_json(data: str) -> ManifestLayout:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ManifestLayout value: {data!r}")
    return cast(ManifestLayout, data)
