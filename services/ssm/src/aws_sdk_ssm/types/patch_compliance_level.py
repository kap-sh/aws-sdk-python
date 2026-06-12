"""Generated from Smithy shape ``com.amazonaws.ssm#PatchComplianceLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

PatchComplianceLevel: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: PatchComplianceLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PatchComplianceLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PatchComplianceLevel value: {data!r}")
    return cast(PatchComplianceLevel, data)
