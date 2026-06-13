"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#MssManifestLayout``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

MssManifestLayout: TypeAlias = Literal[
    "FULL",
    "COMPACT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FULL",
        "COMPACT",
    )
)


def serialize_json(value: MssManifestLayout) -> str:
    return value


def deserialize_json(data: str) -> MssManifestLayout:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MssManifestLayout value: {data!r}")
    return cast(MssManifestLayout, data)
