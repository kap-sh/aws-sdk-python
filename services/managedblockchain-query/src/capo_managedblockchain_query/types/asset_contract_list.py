"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#AssetContractList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.asset_contract

AssetContractList: TypeAlias = list[
    "capo_managedblockchain_query.types.asset_contract.AssetContract"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetContractList) -> list:
    import capo_managedblockchain_query.types.asset_contract

    out: list = []
    for item in value:
        out.append(
            capo_managedblockchain_query.types.asset_contract.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssetContractList:
    import capo_managedblockchain_query.types.asset_contract

    out: AssetContractList = []
    for item in data:
        out.append(
            capo_managedblockchain_query.types.asset_contract.deserialize_json(item)
        )
    return out
