"""Generated from Smithy shape ``com.amazonaws.mediapackage#__listOfHlsManifest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackage.types.hls_manifest

__listOfHlsManifest: TypeAlias = list[
    "capo_mediapackage.types.hls_manifest.HlsManifest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfHlsManifest) -> list:
    import capo_mediapackage.types.hls_manifest

    out: list = []
    for item in value:
        out.append(capo_mediapackage.types.hls_manifest.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfHlsManifest:
    import capo_mediapackage.types.hls_manifest

    out: __listOfHlsManifest = []
    for item in data:
        out.append(capo_mediapackage.types.hls_manifest.deserialize_json(item))
    return out
