"""Generated from Smithy shape ``com.amazonaws.ssm#ComplianceStringFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.compliance_string_filter

ComplianceStringFilterList: TypeAlias = list[
    "aws_sdk_ssm.types.compliance_string_filter.ComplianceStringFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceStringFilterList) -> list:
    import aws_sdk_ssm.types.compliance_string_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.compliance_string_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ComplianceStringFilterList:
    import aws_sdk_ssm.types.compliance_string_filter

    out: ComplianceStringFilterList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.compliance_string_filter.deserialize_aws_json_1_1(item)
        )
    return out
