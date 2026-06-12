"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#BenefitApplicationIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.benefit_application_identifier

BenefitApplicationIdentifierList: TypeAlias = list[
    "aws_sdk_partnercentral_benefits.types.benefit_application_identifier.BenefitApplicationIdentifier"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BenefitApplicationIdentifierList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> BenefitApplicationIdentifierList:
    return list(data)
