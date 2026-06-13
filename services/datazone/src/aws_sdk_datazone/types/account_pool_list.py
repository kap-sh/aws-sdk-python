"""Generated from Smithy shape ``com.amazonaws.datazone#AccountPoolList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.account_pool_id

AccountPoolList: TypeAlias = list[
    "aws_sdk_datazone.types.account_pool_id.AccountPoolId"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountPoolList) -> list:
    return list(value)


def deserialize_json(data: list) -> AccountPoolList:
    return list(data)
