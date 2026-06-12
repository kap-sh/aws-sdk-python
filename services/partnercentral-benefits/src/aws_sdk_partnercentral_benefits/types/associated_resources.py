"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#AssociatedResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.associated_resource

AssociatedResources: TypeAlias = list[
    "aws_sdk_partnercentral_benefits.types.associated_resource.AssociatedResource"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociatedResources) -> list:
    import aws_sdk_partnercentral_benefits.types.associated_resource

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_benefits.types.associated_resource.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AssociatedResources:
    import aws_sdk_partnercentral_benefits.types.associated_resource

    out: AssociatedResources = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_benefits.types.associated_resource.deserialize_aws_json_1_0(
                item
            )
        )
    return out
