"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#PrimaryNeedsFromAws``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.primary_need_from_aws

PrimaryNeedsFromAws: TypeAlias = list[
    "aws_sdk_partnercentral_selling.types.primary_need_from_aws.PrimaryNeedFromAws"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PrimaryNeedsFromAws) -> list:
    import aws_sdk_partnercentral_selling.types.primary_need_from_aws

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_selling.types.primary_need_from_aws.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PrimaryNeedsFromAws:
    import aws_sdk_partnercentral_selling.types.primary_need_from_aws

    out: PrimaryNeedsFromAws = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_selling.types.primary_need_from_aws.deserialize_aws_json_1_0(
                item
            )
        )
    return out
