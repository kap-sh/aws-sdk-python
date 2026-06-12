"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#Statuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.benefit_application_status

Statuses: TypeAlias = list[
    "aws_sdk_partnercentral_benefits.types.benefit_application_status.BenefitApplicationStatus"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Statuses) -> list:
    import aws_sdk_partnercentral_benefits.types.benefit_application_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_benefits.types.benefit_application_status.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> Statuses:
    import aws_sdk_partnercentral_benefits.types.benefit_application_status

    out: Statuses = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_benefits.types.benefit_application_status.deserialize_aws_json_1_0(
                item
            )
        )
    return out
