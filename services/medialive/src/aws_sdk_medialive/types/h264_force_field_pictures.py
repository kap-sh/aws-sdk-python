"""Generated from Smithy shape ``com.amazonaws.medialive#H264ForceFieldPictures``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H264 Force Field Pictures"""
H264ForceFieldPictures: TypeAlias = Literal[
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


def serialize_json(value: H264ForceFieldPictures) -> str:
    return value


def deserialize_json(data: str) -> H264ForceFieldPictures:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H264ForceFieldPictures value: {data!r}")
    return cast(H264ForceFieldPictures, data)
