"""Generated from Smithy shape ``com.amazonaws.ecr#FindingSeverity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr.errors import DeserializationError

FindingSeverity: TypeAlias = Literal[
    "INFORMATIONAL",
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL",
    "UNDEFINED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INFORMATIONAL",
        "LOW",
        "MEDIUM",
        "HIGH",
        "CRITICAL",
        "UNDEFINED",
    )
)


def serialize_aws_json_1_1(value: FindingSeverity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FindingSeverity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FindingSeverity value: {data!r}")
    return cast(FindingSeverity, data)
