"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#BenefitAllocationStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.benefit_allocation_status

BenefitAllocationStatusList: TypeAlias = list[
    "aws_sdk_partnercentral_benefits.types.benefit_allocation_status.BenefitAllocationStatus"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BenefitAllocationStatusList) -> list:
    import aws_sdk_partnercentral_benefits.types.benefit_allocation_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_benefits.types.benefit_allocation_status.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BenefitAllocationStatusList:
    import aws_sdk_partnercentral_benefits.types.benefit_allocation_status

    out: BenefitAllocationStatusList = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_benefits.types.benefit_allocation_status.deserialize_aws_json_1_0(
                item
            )
        )
    return out
