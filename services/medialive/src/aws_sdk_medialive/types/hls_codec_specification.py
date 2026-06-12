"""Generated from Smithy shape ``com.amazonaws.medialive#HlsCodecSpecification``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls Codec Specification"""
HlsCodecSpecification: TypeAlias = Literal[
    "RFC_4281",
    "RFC_6381",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RFC_4281",
        "RFC_6381",
    )
)


def serialize_json(value: HlsCodecSpecification) -> str:
    return value


def deserialize_json(data: str) -> HlsCodecSpecification:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsCodecSpecification value: {data!r}")
    return cast(HlsCodecSpecification, data)
