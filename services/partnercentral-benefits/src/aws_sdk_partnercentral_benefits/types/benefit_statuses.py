"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#BenefitStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.benefit_status

BenefitStatuses: TypeAlias = list[
    "aws_sdk_partnercentral_benefits.types.benefit_status.BenefitStatus"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BenefitStatuses) -> list:
    import aws_sdk_partnercentral_benefits.types.benefit_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_benefits.types.benefit_status.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BenefitStatuses:
    import aws_sdk_partnercentral_benefits.types.benefit_status

    out: BenefitStatuses = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_benefits.types.benefit_status.deserialize_aws_json_1_0(
                item
            )
        )
    return out
