"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceComplianceSummaryItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.resource_compliance_summary_item

ResourceComplianceSummaryItemList: TypeAlias = list[
    "capo_ssm.types.resource_compliance_summary_item.ResourceComplianceSummaryItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceComplianceSummaryItemList) -> list:
    import capo_ssm.types.resource_compliance_summary_item

    out: list = []
    for item in value:
        out.append(
            capo_ssm.types.resource_compliance_summary_item.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceComplianceSummaryItemList:
    import capo_ssm.types.resource_compliance_summary_item

    out: ResourceComplianceSummaryItemList = []
    for item in data:
        out.append(
            capo_ssm.types.resource_compliance_summary_item.deserialize_aws_json_1_1(
                item
            )
        )
    return out
