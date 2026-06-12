"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationComplianceSeverity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

AssociationComplianceSeverity: TypeAlias = Literal[
    "CRITICAL",
    "HIGH",
    "MEDIUM",
    "LOW",
    "UNSPECIFIED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CRITICAL",
        "HIGH",
        "MEDIUM",
        "LOW",
        "UNSPECIFIED",
    )
)


def serialize_aws_json_1_1(value: AssociationComplianceSeverity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssociationComplianceSeverity:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AssociationComplianceSeverity value: {data!r}"
        )
    return cast(AssociationComplianceSeverity, data)
