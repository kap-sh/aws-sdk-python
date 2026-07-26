"""Generated from Smithy shape ``com.amazonaws.medialive#SmoothGroupStreamManifestBehavior``."""

from typing import Literal, TypeAlias, cast

"""Smooth Group Stream Manifest Behavior"""
SmoothGroupStreamManifestBehavior: TypeAlias = Literal[
    "DO_NOT_SEND",
    "SEND",
]


# --- restJson1 ser/de ---
def serialize_json(value: SmoothGroupStreamManifestBehavior) -> str:
    return value


def deserialize_json(data: str) -> SmoothGroupStreamManifestBehavior:
    return cast(SmoothGroupStreamManifestBehavior, data)
