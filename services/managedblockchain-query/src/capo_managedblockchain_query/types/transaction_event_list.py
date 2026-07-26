"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#TransactionEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.transaction_event

TransactionEventList: TypeAlias = list[
    "capo_managedblockchain_query.types.transaction_event.TransactionEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: TransactionEventList) -> list:
    import capo_managedblockchain_query.types.transaction_event

    out: list = []
    for item in value:
        out.append(
            capo_managedblockchain_query.types.transaction_event.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TransactionEventList:
    import capo_managedblockchain_query.types.transaction_event

    out: TransactionEventList = []
    for item in data:
        out.append(
            capo_managedblockchain_query.types.transaction_event.deserialize_json(item)
        )
    return out
