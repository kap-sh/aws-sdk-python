"""Generated from Smithy shape ``com.amazonaws.mediapackage#ManifestLayout``."""

from typing import Literal, TypeAlias, cast

ManifestLayout: TypeAlias = Literal[
    "FULL",
    "COMPACT",
    "DRM_TOP_LEVEL_COMPACT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ManifestLayout) -> str:
    return value


def deserialize_json(data: str) -> ManifestLayout:
    return cast(ManifestLayout, data)
