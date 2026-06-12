"""Generated from Smithy shape ``com.amazonaws.medialive#H265SubGopLength``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H265 Sub Gop Length"""
H265SubGopLength: TypeAlias = Literal[
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


def serialize_json(value: H265SubGopLength) -> str:
    return value


def deserialize_json(data: str) -> H265SubGopLength:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265SubGopLength value: {data!r}")
    return cast(H265SubGopLength, data)
