"""Generated from Smithy shape ``com.amazonaws.medialive#HlsWebdavHttpTransferMode``."""

from typing import Literal, TypeAlias, cast

"""Hls Webdav Http Transfer Mode"""
HlsWebdavHttpTransferMode: TypeAlias = Literal[
    "CHUNKED",
    "NON_CHUNKED",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsWebdavHttpTransferMode) -> str:
    return value


def deserialize_json(data: str) -> HlsWebdavHttpTransferMode:
    return cast(HlsWebdavHttpTransferMode, data)
