"""Generated from Smithy shape ``com.amazonaws.ssm#ComplianceItemEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.compliance_item_entry

ComplianceItemEntryList: TypeAlias = list[
    "aws_sdk_ssm.types.compliance_item_entry.ComplianceItemEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceItemEntryList) -> list:
    import aws_sdk_ssm.types.compliance_item_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.compliance_item_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ComplianceItemEntryList:
    import aws_sdk_ssm.types.compliance_item_entry

    out: ComplianceItemEntryList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.compliance_item_entry.deserialize_aws_json_1_1(item)
        )
    return out
