"""Generated from Smithy shape ``com.amazonaws.ssm#AccountIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.account_id

AccountIdList: TypeAlias = list["capo_ssm.types.account_id.AccountId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AccountIdList:
    return list(data)
