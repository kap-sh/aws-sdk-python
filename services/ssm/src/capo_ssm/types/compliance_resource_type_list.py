"""Generated from Smithy shape ``com.amazonaws.ssm#ComplianceResourceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.compliance_resource_type

ComplianceResourceTypeList: TypeAlias = list[
    "capo_ssm.types.compliance_resource_type.ComplianceResourceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceResourceTypeList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ComplianceResourceTypeList:
    return [item for item in data if item is not None]
