"""Generated from Smithy shape ``com.amazonaws.ssm#ComplianceSeverity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

ComplianceSeverity: TypeAlias = Literal[
    "CRITICAL",
    "HIGH",
    "MEDIUM",
    "LOW",
    "INFORMATIONAL",
    "UNSPECIFIED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CRITICAL",
        "HIGH",
        "MEDIUM",
        "LOW",
        "INFORMATIONAL",
        "UNSPECIFIED",
    )
)


def serialize_aws_json_1_1(value: ComplianceSeverity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComplianceSeverity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComplianceSeverity value: {data!r}")
    return cast(ComplianceSeverity, data)
