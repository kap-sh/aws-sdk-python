"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackComplianceType``."""

from typing import Literal, TypeAlias, cast

ConformancePackComplianceType: TypeAlias = Literal[
    "COMPLIANT",
    "NON_COMPLIANT",
    "INSUFFICIENT_DATA",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackComplianceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConformancePackComplianceType:
    return cast(ConformancePackComplianceType, data)
