"""Generated from Smithy shape ``com.amazonaws.medialive#HlsAkamaiHttpTransferMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls Akamai Http Transfer Mode"""
HlsAkamaiHttpTransferMode: TypeAlias = Literal[
    "CHUNKED",
    "NON_CHUNKED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CHUNKED",
        "NON_CHUNKED",
    )
)


def serialize_json(value: HlsAkamaiHttpTransferMode) -> str:
    return value


def deserialize_json(data: str) -> HlsAkamaiHttpTransferMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsAkamaiHttpTransferMode value: {data!r}")
    return cast(HlsAkamaiHttpTransferMode, data)
