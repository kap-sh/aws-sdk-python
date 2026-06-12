"""Generated from Smithy shape ``com.amazonaws.ssm#ComplianceItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.compliance_item

ComplianceItemList: TypeAlias = list["aws_sdk_ssm.types.compliance_item.ComplianceItem"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceItemList) -> list:
    import aws_sdk_ssm.types.compliance_item

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.compliance_item.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ComplianceItemList:
    import aws_sdk_ssm.types.compliance_item

    out: ComplianceItemList = []
    for item in data:
        out.append(aws_sdk_ssm.types.compliance_item.deserialize_aws_json_1_1(item))
    return out
