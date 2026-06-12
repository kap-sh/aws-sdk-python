"""Generated from Smithy shape ``com.amazonaws.medialive#H264GopBReference``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H264 Gop BReference"""
H264GopBReference: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: H264GopBReference) -> str:
    return value


def deserialize_json(data: str) -> H264GopBReference:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H264GopBReference value: {data!r}")
    return cast(H264GopBReference, data)
