"""Generated from Smithy shape ``com.amazonaws.medialive#H265GopBReference``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H265 Gop BReference"""
H265GopBReference: TypeAlias = Literal[
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


def serialize_json(value: H265GopBReference) -> str:
    return value


def deserialize_json(data: str) -> H265GopBReference:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265GopBReference value: {data!r}")
    return cast(H265GopBReference, data)
