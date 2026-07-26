"""Generated from Smithy shape ``com.amazonaws.ssm#PatchComplianceDataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.patch_compliance_data

PatchComplianceDataList: TypeAlias = list[
    "capo_ssm.types.patch_compliance_data.PatchComplianceData"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchComplianceDataList) -> list:
    import capo_ssm.types.patch_compliance_data

    out: list = []
    for item in value:
        out.append(capo_ssm.types.patch_compliance_data.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PatchComplianceDataList:
    import capo_ssm.types.patch_compliance_data

    out: PatchComplianceDataList = []
    for item in data:
        out.append(capo_ssm.types.patch_compliance_data.deserialize_aws_json_1_1(item))
    return out
