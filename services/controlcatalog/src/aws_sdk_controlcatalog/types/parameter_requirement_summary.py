"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ParameterRequirementSummary``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_controlcatalog.errors import DeserializationError

ParameterRequirementSummary: TypeAlias = Literal[
    "REQUIRED",
    "OPTIONAL",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUIRED",
        "OPTIONAL",
        "NONE",
    )
)


def serialize_json(value: ParameterRequirementSummary) -> str:
    return value


def deserialize_json(data: str) -> ParameterRequirementSummary:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ParameterRequirementSummary value: {data!r}"
        )
    return cast(ParameterRequirementSummary, data)
