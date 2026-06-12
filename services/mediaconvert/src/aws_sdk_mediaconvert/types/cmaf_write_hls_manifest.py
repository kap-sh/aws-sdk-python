"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmafWriteHLSManifest``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""When set to ENABLED, an Apple HLS manifest will be generated for this output."""
CmafWriteHLSManifest: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: CmafWriteHLSManifest) -> str:
    return value


def deserialize_json(data: str) -> CmafWriteHLSManifest:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CmafWriteHLSManifest value: {data!r}")
    return cast(CmafWriteHLSManifest, data)
