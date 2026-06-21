"""Generated from Smithy shape ``com.amazonaws.medialive#HlsAkamaiHttpTransferMode``."""

from typing import Literal, TypeAlias, cast

"""Hls Akamai Http Transfer Mode"""
HlsAkamaiHttpTransferMode: TypeAlias = Literal[
    "CHUNKED",
    "NON_CHUNKED",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsAkamaiHttpTransferMode) -> str:
    return value


def deserialize_json(data: str) -> HlsAkamaiHttpTransferMode:
    return cast(HlsAkamaiHttpTransferMode, data)
