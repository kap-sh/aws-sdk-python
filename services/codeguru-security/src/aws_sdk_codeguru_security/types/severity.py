"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#Severity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeguru_security.errors import DeserializationError

Severity: TypeAlias = Literal[
    "Critical",
    "High",
    "Medium",
    "Low",
    "Info",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Critical",
        "High",
        "Medium",
        "Low",
        "Info",
    )
)


def serialize_json(value: Severity) -> str:
    return value


def deserialize_json(data: str) -> Severity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Severity value: {data!r}")
    return cast(Severity, data)
