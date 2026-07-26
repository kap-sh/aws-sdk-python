"""Generated from Smithy shape ``com.amazonaws.configservice#ComplianceType``."""

from typing import Literal, TypeAlias, cast

ComplianceType: TypeAlias = Literal[
    "COMPLIANT",
    "NON_COMPLIANT",
    "NOT_APPLICABLE",
    "INSUFFICIENT_DATA",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComplianceType:
    return cast(ComplianceType, data)
