"""Generated from Smithy shape ``com.amazonaws.entityresolution#AwsAccountIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.aws_account_id

AwsAccountIdList: TypeAlias = list[
    "aws_sdk_entityresolution.types.aws_account_id.AwsAccountId"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsAccountIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AwsAccountIdList:
    return list(data)
