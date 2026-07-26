"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#MssManifestLayout``."""

from typing import Literal, TypeAlias, cast

MssManifestLayout: TypeAlias = Literal[
    "FULL",
    "COMPACT",
]


# --- restJson1 ser/de ---
def serialize_json(value: MssManifestLayout) -> str:
    return value


def deserialize_json(data: str) -> MssManifestLayout:
    return cast(MssManifestLayout, data)
