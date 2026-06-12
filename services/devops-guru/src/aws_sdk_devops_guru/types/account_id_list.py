"""Generated from Smithy shape ``com.amazonaws.devopsguru#AccountIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.aws_account_id

AccountIdList: TypeAlias = list["aws_sdk_devops_guru.types.aws_account_id.AwsAccountId"]


# --- restJson1 ser/de ---
def serialize_json(value: AccountIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AccountIdList:
    return list(data)
