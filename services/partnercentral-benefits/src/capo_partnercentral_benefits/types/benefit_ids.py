"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#BenefitIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.benefit_id

BenefitIds: TypeAlias = list["capo_partnercentral_benefits.types.benefit_id.BenefitId"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BenefitIds) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> BenefitIds:
    return list(data)
