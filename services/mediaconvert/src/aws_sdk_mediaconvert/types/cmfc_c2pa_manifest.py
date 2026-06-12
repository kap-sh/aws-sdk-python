"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmfcC2paManifest``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""When enabled, a C2PA compliant manifest will be generated, signed and embeded in the output. For more information on C2PA, see https://c2pa.org/specifications/specifications/2.1/index.html"""
CmfcC2paManifest: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCLUDE",
        "EXCLUDE",
    )
)


def serialize_json(value: CmfcC2paManifest) -> str:
    return value


def deserialize_json(data: str) -> CmfcC2paManifest:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CmfcC2paManifest value: {data!r}")
    return cast(CmfcC2paManifest, data)
