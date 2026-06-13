"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#BatchGetTokenBalanceOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.batch_get_token_balance_output_item

BatchGetTokenBalanceOutputList: TypeAlias = list[
    "aws_sdk_managedblockchain_query.types.batch_get_token_balance_output_item.BatchGetTokenBalanceOutputItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTokenBalanceOutputList) -> list:
    import aws_sdk_managedblockchain_query.types.batch_get_token_balance_output_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_managedblockchain_query.types.batch_get_token_balance_output_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetTokenBalanceOutputList:
    import aws_sdk_managedblockchain_query.types.batch_get_token_balance_output_item

    out: BatchGetTokenBalanceOutputList = []
    for item in data:
        out.append(
            aws_sdk_managedblockchain_query.types.batch_get_token_balance_output_item.deserialize_json(
                item
            )
        )
    return out
