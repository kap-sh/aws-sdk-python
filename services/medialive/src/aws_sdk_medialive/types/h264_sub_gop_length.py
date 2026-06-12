"""Generated from Smithy shape ``com.amazonaws.medialive#H264SubGopLength``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H264 Sub Gop Length"""
H264SubGopLength: TypeAlias = Literal[
    "DYNAMIC",
    "FIXED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DYNAMIC",
        "FIXED",
    )
)


def serialize_json(value: H264SubGopLength) -> str:
    return value


def deserialize_json(data: str) -> H264SubGopLength:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H264SubGopLength value: {data!r}")
    return cast(H264SubGopLength, data)
