"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#TransactionOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.transaction_output_item

TransactionOutputList: TypeAlias = list[
    "capo_managedblockchain_query.types.transaction_output_item.TransactionOutputItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: TransactionOutputList) -> list:
    import capo_managedblockchain_query.types.transaction_output_item

    out: list = []
    for item in value:
        out.append(
            capo_managedblockchain_query.types.transaction_output_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TransactionOutputList:
    import capo_managedblockchain_query.types.transaction_output_item

    out: TransactionOutputList = []
    for item in data:
        out.append(
            capo_managedblockchain_query.types.transaction_output_item.deserialize_json(
                item
            )
        )
    return out
