"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#TokenBalanceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.token_balance

TokenBalanceList: TypeAlias = list[
    "aws_sdk_managedblockchain_query.types.token_balance.TokenBalance"
]


# --- restJson1 ser/de ---
def serialize_json(value: TokenBalanceList) -> list:
    import aws_sdk_managedblockchain_query.types.token_balance

    out: list = []
    for item in value:
        out.append(
            aws_sdk_managedblockchain_query.types.token_balance.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TokenBalanceList:
    import aws_sdk_managedblockchain_query.types.token_balance

    out: TokenBalanceList = []
    for item in data:
        out.append(
            aws_sdk_managedblockchain_query.types.token_balance.deserialize_json(item)
        )
    return out
