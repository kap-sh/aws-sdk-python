"""Generated from Smithy shape ``com.amazonaws.medialive#H265GopSizeUnits``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H265 Gop Size Units"""
H265GopSizeUnits: TypeAlias = Literal[
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


def serialize_json(value: H265GopSizeUnits) -> str:
    return value


def deserialize_json(data: str) -> H265GopSizeUnits:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265GopSizeUnits value: {data!r}")
    return cast(H265GopSizeUnits, data)
