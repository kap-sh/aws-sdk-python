"""Generated from Smithy shape ``com.amazonaws.pi#Severity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pi.errors import DeserializationError

Severity: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOW",
        "MEDIUM",
        "HIGH",
    )
)


def serialize_aws_json_1_1(value: Severity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Severity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Severity value: {data!r}")
    return cast(Severity, data)
