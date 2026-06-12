"""Generated from Smithy shape ``com.amazonaws.inspector#Severity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector.errors import DeserializationError

Severity: TypeAlias = Literal[
    "Low",
    "Medium",
    "High",
    "Informational",
    "Undefined",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Low",
        "Medium",
        "High",
        "Informational",
        "Undefined",
    )
)


def serialize_aws_json_1_1(value: Severity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Severity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Severity value: {data!r}")
    return cast(Severity, data)
