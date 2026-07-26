"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#ChainAddresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.chain_address

ChainAddresses: TypeAlias = list[
    "capo_managedblockchain_query.types.chain_address.ChainAddress"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChainAddresses) -> list:
    return list(value)


def deserialize_json(data: list) -> ChainAddresses:
    return list(data)
