"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#Severity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeguru_reviewer.errors import DeserializationError

Severity: TypeAlias = Literal[
    "Info",
    "Low",
    "Medium",
    "High",
    "Critical",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Info",
        "Low",
        "Medium",
        "High",
        "Critical",
    )
)


def serialize_json(value: Severity) -> str:
    return value


def deserialize_json(data: str) -> Severity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Severity value: {data!r}")
    return cast(Severity, data)
