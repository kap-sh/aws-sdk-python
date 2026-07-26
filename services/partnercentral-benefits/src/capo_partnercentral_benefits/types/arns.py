"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#Arns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.arn

Arns: TypeAlias = list["capo_partnercentral_benefits.types.arn.Arn"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Arns) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> Arns:
    return list(data)
