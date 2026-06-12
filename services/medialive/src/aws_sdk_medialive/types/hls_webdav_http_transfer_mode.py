"""Generated from Smithy shape ``com.amazonaws.medialive#HlsWebdavHttpTransferMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls Webdav Http Transfer Mode"""
HlsWebdavHttpTransferMode: TypeAlias = Literal[
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


def serialize_json(value: HlsWebdavHttpTransferMode) -> str:
    return value


def deserialize_json(data: str) -> HlsWebdavHttpTransferMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsWebdavHttpTransferMode value: {data!r}")
    return cast(HlsWebdavHttpTransferMode, data)
