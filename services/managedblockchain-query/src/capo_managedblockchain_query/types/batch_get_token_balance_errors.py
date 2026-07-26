"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#BatchGetTokenBalanceErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.batch_get_token_balance_error_item

BatchGetTokenBalanceErrors: TypeAlias = list[
    "capo_managedblockchain_query.types.batch_get_token_balance_error_item.BatchGetTokenBalanceErrorItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTokenBalanceErrors) -> list:
    import capo_managedblockchain_query.types.batch_get_token_balance_error_item

    out: list = []
    for item in value:
        out.append(
            capo_managedblockchain_query.types.batch_get_token_balance_error_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetTokenBalanceErrors:
    import capo_managedblockchain_query.types.batch_get_token_balance_error_item

    out: BatchGetTokenBalanceErrors = []
    for item in data:
        out.append(
            capo_managedblockchain_query.types.batch_get_token_balance_error_item.deserialize_json(
                item
            )
        )
    return out
