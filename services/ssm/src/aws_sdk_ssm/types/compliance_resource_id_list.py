"""Generated from Smithy shape ``com.amazonaws.ssm#ComplianceResourceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.compliance_resource_id

ComplianceResourceIdList: TypeAlias = list[
    "aws_sdk_ssm.types.compliance_resource_id.ComplianceResourceId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceResourceIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ComplianceResourceIdList:
    return list(data)
