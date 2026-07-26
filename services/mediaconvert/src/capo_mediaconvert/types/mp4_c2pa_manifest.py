"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mp4C2paManifest``."""

from typing import Literal, TypeAlias, cast

"""When enabled, a C2PA compliant manifest will be generated, signed and embeded in the output. For more information on C2PA, see https://c2pa.org/specifications/specifications/2.1/index.html"""
Mp4C2paManifest: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mp4C2paManifest) -> str:
    return value


def deserialize_json(data: str) -> Mp4C2paManifest:
    return cast(Mp4C2paManifest, data)
