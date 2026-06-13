"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#ContractIdentifier``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.chain_address
    import aws_sdk_managedblockchain_query.types.query_network


class ContractIdentifier(TypedDict):
    network: "aws_sdk_managedblockchain_query.types.query_network.QueryNetwork"
    """<p>The blockchain network of the contract.</p>"""
    contract_address: "aws_sdk_managedblockchain_query.types.chain_address.ChainAddress"
    """<p>Container for the blockchain address about a contract.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContractIdentifier) -> dict:
    out: dict = {}
    out["network"] = value["network"]
    out["contractAddress"] = value["contract_address"]
    return out


def deserialize_json(data: dict) -> ContractIdentifier:
    out: ContractIdentifier = {}  # type: ignore[typeddict-item]
    if "network" in data:
        out["network"] = data["network"]
    else:
        raise DeserializationError("ContractIdentifier.network required")
    if "contractAddress" in data:
        out["contract_address"] = data["contractAddress"]
    else:
        raise DeserializationError("ContractIdentifier.contract_address required")
    return out
