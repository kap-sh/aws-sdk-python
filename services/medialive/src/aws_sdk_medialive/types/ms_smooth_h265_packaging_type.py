"""Generated from Smithy shape ``com.amazonaws.medialive#MsSmoothH265PackagingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Ms Smooth H265 Packaging Type"""
MsSmoothH265PackagingType: TypeAlias = Literal[
    "HEV1",
    "HVC1",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HEV1",
        "HVC1",
    )
)


def serialize_json(value: MsSmoothH265PackagingType) -> str:
    return value


def deserialize_json(data: str) -> MsSmoothH265PackagingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MsSmoothH265PackagingType value: {data!r}")
    return cast(MsSmoothH265PackagingType, data)
