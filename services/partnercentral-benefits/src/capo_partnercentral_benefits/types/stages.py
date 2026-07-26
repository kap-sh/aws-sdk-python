"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#Stages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.benefit_application_stage

Stages: TypeAlias = list[
    "capo_partnercentral_benefits.types.benefit_application_stage.BenefitApplicationStage"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Stages) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> Stages:
    return list(data)
