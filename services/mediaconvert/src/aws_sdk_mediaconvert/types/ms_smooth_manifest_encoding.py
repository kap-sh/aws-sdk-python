"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MsSmoothManifestEncoding``."""

from typing import Literal, TypeAlias, cast

"""Use Manifest encoding to specify the encoding format for the server and client manifest. Valid options are utf8 and utf16."""
MsSmoothManifestEncoding: TypeAlias = Literal[
    "UTF8",
    "UTF16",
]


# --- restJson1 ser/de ---
def serialize_json(value: MsSmoothManifestEncoding) -> str:
    return value


def deserialize_json(data: str) -> MsSmoothManifestEncoding:
    return cast(MsSmoothManifestEncoding, data)
