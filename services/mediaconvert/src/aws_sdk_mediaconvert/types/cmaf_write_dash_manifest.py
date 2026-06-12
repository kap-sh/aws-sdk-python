"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmafWriteDASHManifest``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""When set to ENABLED, a DASH MPD manifest will be generated for this output."""
CmafWriteDASHManifest: TypeAlias = Literal[
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


def serialize_json(value: CmafWriteDASHManifest) -> str:
    return value


def deserialize_json(data: str) -> CmafWriteDASHManifest:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CmafWriteDASHManifest value: {data!r}")
    return cast(CmafWriteDASHManifest, data)
