"""Generated from Smithy shape ``com.amazonaws.fms#PolicyComplianceStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.policy_compliance_status

PolicyComplianceStatusList: TypeAlias = list[
    "aws_sdk_fms.types.policy_compliance_status.PolicyComplianceStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyComplianceStatusList) -> list:
    import aws_sdk_fms.types.policy_compliance_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_fms.types.policy_compliance_status.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PolicyComplianceStatusList:
    import aws_sdk_fms.types.policy_compliance_status

    out: PolicyComplianceStatusList = []
    for item in data:
        out.append(
            aws_sdk_fms.types.policy_compliance_status.deserialize_aws_json_1_1(item)
        )
    return out
