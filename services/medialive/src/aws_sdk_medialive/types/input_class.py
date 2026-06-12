"""Generated from Smithy shape ``com.amazonaws.medialive#InputClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""A standard input has two sources and a single pipeline input only has one."""
InputClass: TypeAlias = Literal[
    "STANDARD",
    "SINGLE_PIPELINE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "SINGLE_PIPELINE",
    )
)


def serialize_json(value: InputClass) -> str:
    return value


def deserialize_json(data: str) -> InputClass:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputClass value: {data!r}")
    return cast(InputClass, data)
