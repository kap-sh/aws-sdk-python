"""Generated from Smithy shape ``com.amazonaws.fis#EmptyTargetResolutionMode``."""

from typing import Literal, TypeAlias, cast

EmptyTargetResolutionMode: TypeAlias = Literal[
    "fail",
    "skip",
]


# --- restJson1 ser/de ---
def serialize_json(value: EmptyTargetResolutionMode) -> str:
    return value


def deserialize_json(data: str) -> EmptyTargetResolutionMode:
    return cast(EmptyTargetResolutionMode, data)
