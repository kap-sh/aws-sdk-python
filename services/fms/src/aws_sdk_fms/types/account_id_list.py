"""Generated from Smithy shape ``com.amazonaws.fms#AccountIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.aws_account_id

AccountIdList: TypeAlias = list["aws_sdk_fms.types.aws_account_id.AWSAccountId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AccountIdList:
    return list(data)
