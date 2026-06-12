"""Generated from Smithy shape ``com.amazonaws.fis#EmptyTargetResolutionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fis.errors import DeserializationError

EmptyTargetResolutionMode: TypeAlias = Literal[
    "fail",
    "skip",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "fail",
        "skip",
    )
)


def serialize_json(value: EmptyTargetResolutionMode) -> str:
    return value


def deserialize_json(data: str) -> EmptyTargetResolutionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EmptyTargetResolutionMode value: {data!r}")
    return cast(EmptyTargetResolutionMode, data)
