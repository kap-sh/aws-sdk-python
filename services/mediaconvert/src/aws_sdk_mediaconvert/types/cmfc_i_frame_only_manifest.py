"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmfcIFrameOnlyManifest``."""

from typing import Literal, TypeAlias, cast

"""Choose Include to have MediaConvert generate an HLS child manifest that lists only the I-frames for this rendition, in addition to your regular manifest for this rendition. You might use this manifest as part of a workflow that creates preview functions for your video. MediaConvert adds both the I-frame only child manifest and the regular child manifest to the parent manifest. When you don't need the I-frame only child manifest, keep the default value Exclude."""
CmfcIFrameOnlyManifest: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: CmfcIFrameOnlyManifest) -> str:
    return value


def deserialize_json(data: str) -> CmfcIFrameOnlyManifest:
    return cast(CmfcIFrameOnlyManifest, data)
