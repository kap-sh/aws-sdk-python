"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsAccountIdOrAliasList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.aws_account

AwsAccountIdOrAliasList: TypeAlias = list[
    "aws_sdk_partnercentral_selling.types.aws_account.AwsAccount"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsAccountIdOrAliasList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> AwsAccountIdOrAliasList:
    return list(data)
