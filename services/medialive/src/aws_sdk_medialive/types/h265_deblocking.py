"""Generated from Smithy shape ``com.amazonaws.medialive#H265Deblocking``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H265 Deblocking"""
H265Deblocking: TypeAlias = Literal[
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


def serialize_json(value: H265Deblocking) -> str:
    return value


def deserialize_json(data: str) -> H265Deblocking:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265Deblocking value: {data!r}")
    return cast(H265Deblocking, data)
