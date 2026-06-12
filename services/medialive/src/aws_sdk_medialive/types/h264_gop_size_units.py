"""Generated from Smithy shape ``com.amazonaws.medialive#H264GopSizeUnits``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H264 Gop Size Units"""
H264GopSizeUnits: TypeAlias = Literal[
    "FRAMES",
    "SECONDS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FRAMES",
        "SECONDS",
    )
)


def serialize_json(value: H264GopSizeUnits) -> str:
    return value


def deserialize_json(data: str) -> H264GopSizeUnits:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H264GopSizeUnits value: {data!r}")
    return cast(H264GopSizeUnits, data)
