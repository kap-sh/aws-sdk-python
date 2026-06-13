"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ControlParameterRequirement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_controlcatalog.errors import DeserializationError

ControlParameterRequirement: TypeAlias = Literal[
    "REQUIRED",
    "OPTIONAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUIRED",
        "OPTIONAL",
    )
)


def serialize_json(value: ControlParameterRequirement) -> str:
    return value


def deserialize_json(data: str) -> ControlParameterRequirement:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ControlParameterRequirement value: {data!r}"
        )
    return cast(ControlParameterRequirement, data)
