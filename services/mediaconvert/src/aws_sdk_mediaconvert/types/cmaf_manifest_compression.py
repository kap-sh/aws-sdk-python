"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmafManifestCompression``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""When set to GZIP, compresses HLS playlist."""
CmafManifestCompression: TypeAlias = Literal[
    "GZIP",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GZIP",
        "NONE",
    )
)


def serialize_json(value: CmafManifestCompression) -> str:
    return value


def deserialize_json(data: str) -> CmafManifestCompression:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CmafManifestCompression value: {data!r}")
    return cast(CmafManifestCompression, data)
