"""Generated from Smithy shape ``com.amazonaws.ssm#ComplianceSummaryItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.compliance_summary_item

ComplianceSummaryItemList: TypeAlias = list[
    "capo_ssm.types.compliance_summary_item.ComplianceSummaryItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceSummaryItemList) -> list:
    import capo_ssm.types.compliance_summary_item

    out: list = []
    for item in value:
        out.append(capo_ssm.types.compliance_summary_item.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ComplianceSummaryItemList:
    import capo_ssm.types.compliance_summary_item

    out: ComplianceSummaryItemList = []
    for item in data:
        out.append(
            capo_ssm.types.compliance_summary_item.deserialize_aws_json_1_1(item)
        )
    return out
