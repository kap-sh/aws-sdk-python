"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#TokenBalanceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.token_balance

TokenBalanceList: TypeAlias = list[
    "capo_managedblockchain_query.types.token_balance.TokenBalance"
]


# --- restJson1 ser/de ---
def serialize_json(value: TokenBalanceList) -> list:
    import capo_managedblockchain_query.types.token_balance

    out: list = []
    for item in value:
        out.append(
            capo_managedblockchain_query.types.token_balance.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TokenBalanceList:
    import capo_managedblockchain_query.types.token_balance

    out: TokenBalanceList = []
    for item in data:
        out.append(
            capo_managedblockchain_query.types.token_balance.deserialize_json(item)
        )
    return out
