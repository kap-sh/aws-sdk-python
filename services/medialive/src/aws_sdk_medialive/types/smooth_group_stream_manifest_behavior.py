"""Generated from Smithy shape ``com.amazonaws.medialive#SmoothGroupStreamManifestBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Smooth Group Stream Manifest Behavior"""
SmoothGroupStreamManifestBehavior: TypeAlias = Literal[
    "DO_NOT_SEND",
    "SEND",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DO_NOT_SEND",
        "SEND",
    )
)


def serialize_json(value: SmoothGroupStreamManifestBehavior) -> str:
    return value


def deserialize_json(data: str) -> SmoothGroupStreamManifestBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SmoothGroupStreamManifestBehavior value: {data!r}"
        )
    return cast(SmoothGroupStreamManifestBehavior, data)
