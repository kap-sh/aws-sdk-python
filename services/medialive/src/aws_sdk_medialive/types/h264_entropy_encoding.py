"""Generated from Smithy shape ``com.amazonaws.medialive#H264EntropyEncoding``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H264 Entropy Encoding"""
H264EntropyEncoding: TypeAlias = Literal[
    "CABAC",
    "CAVLC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CABAC",
        "CAVLC",
    )
)


def serialize_json(value: H264EntropyEncoding) -> str:
    return value


def deserialize_json(data: str) -> H264EntropyEncoding:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H264EntropyEncoding value: {data!r}")
    return cast(H264EntropyEncoding, data)
