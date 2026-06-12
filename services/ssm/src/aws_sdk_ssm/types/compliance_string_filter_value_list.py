"""Generated from Smithy shape ``com.amazonaws.ssm#ComplianceStringFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.compliance_filter_value

ComplianceStringFilterValueList: TypeAlias = list[
    "aws_sdk_ssm.types.compliance_filter_value.ComplianceFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceStringFilterValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ComplianceStringFilterValueList:
    return list(data)
