"""Generated from Smithy shape ``com.amazonaws.ssm#ComplianceQueryOperatorType``."""

from typing import Literal, TypeAlias, cast

ComplianceQueryOperatorType: TypeAlias = Literal[
    "EQUAL",
    "NOT_EQUAL",
    "BEGIN_WITH",
    "LESS_THAN",
    "GREATER_THAN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceQueryOperatorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComplianceQueryOperatorType:
    return cast(ComplianceQueryOperatorType, data)
