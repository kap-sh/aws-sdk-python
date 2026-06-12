"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#AwsAccountIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.aws_account_id

AwsAccountIds: TypeAlias = list[
    "aws_sdk_global_accelerator.types.aws_account_id.AwsAccountId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AwsAccountIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AwsAccountIds:
    return list(data)
