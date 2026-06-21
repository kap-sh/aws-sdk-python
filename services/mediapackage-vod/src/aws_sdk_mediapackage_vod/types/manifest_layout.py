"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#ManifestLayout``."""

from typing import Literal, TypeAlias, cast

ManifestLayout: TypeAlias = Literal[
    "FULL",
    "COMPACT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ManifestLayout) -> str:
    return value


def deserialize_json(data: str) -> ManifestLayout:
    return cast(ManifestLayout, data)
