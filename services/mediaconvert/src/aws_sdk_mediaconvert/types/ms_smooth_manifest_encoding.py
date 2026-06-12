"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MsSmoothManifestEncoding``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Use Manifest encoding to specify the encoding format for the server and client manifest. Valid options are utf8 and utf16."""
MsSmoothManifestEncoding: TypeAlias = Literal[
    "UTF8",
    "UTF16",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UTF8",
        "UTF16",
    )
)


def serialize_json(value: MsSmoothManifestEncoding) -> str:
    return value


def deserialize_json(data: str) -> MsSmoothManifestEncoding:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MsSmoothManifestEncoding value: {data!r}")
    return cast(MsSmoothManifestEncoding, data)
