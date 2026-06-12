"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsIFrameOnlyManifest``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Generate a variant manifest that lists only the I-frames for this rendition. You might use this manifest as part of a workflow that creates preview functions for your video. MediaConvert adds both the I-frame only variant manifest and the regular variant manifest to the multivariant manifest. To have MediaConvert write a variant manifest that references I-frames from your output content using EXT-X-BYTERANGE tags: Choose Include. To have MediaConvert output I-frames as single frame TS files and a corresponding variant manifest that references them: Choose Include as TS. When you don't need the I-frame only variant manifest: Keep the default value, Exclude."""
HlsIFrameOnlyManifest: TypeAlias = Literal[
    "INCLUDE",
    "INCLUDE_AS_TS",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCLUDE",
        "INCLUDE_AS_TS",
        "EXCLUDE",
    )
)


def serialize_json(value: HlsIFrameOnlyManifest) -> str:
    return value


def deserialize_json(data: str) -> HlsIFrameOnlyManifest:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsIFrameOnlyManifest value: {data!r}")
    return cast(HlsIFrameOnlyManifest, data)
