"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#BenefitIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.benefit_id

BenefitIdentifiers: TypeAlias = list[
    "aws_sdk_partnercentral_benefits.types.benefit_id.BenefitId"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BenefitIdentifiers) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> BenefitIdentifiers:
    return list(data)
