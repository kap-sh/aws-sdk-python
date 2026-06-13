"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#GetTokenBalanceInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.batch_get_token_balance_input_item

GetTokenBalanceInputList: TypeAlias = list[
    "aws_sdk_managedblockchain_query.types.batch_get_token_balance_input_item.BatchGetTokenBalanceInputItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: GetTokenBalanceInputList) -> list:
    import aws_sdk_managedblockchain_query.types.batch_get_token_balance_input_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_managedblockchain_query.types.batch_get_token_balance_input_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GetTokenBalanceInputList:
    import aws_sdk_managedblockchain_query.types.batch_get_token_balance_input_item

    out: GetTokenBalanceInputList = []
    for item in data:
        out.append(
            aws_sdk_managedblockchain_query.types.batch_get_token_balance_input_item.deserialize_json(
                item
            )
        )
    return out
