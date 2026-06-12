"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#AssetContract``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_managedblockchain_query.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.chain_address
    import aws_sdk_managedblockchain_query.types.contract_identifier
    import aws_sdk_managedblockchain_query.types.query_token_standard

class AssetContract(TypedDict):
    contract_identifier: "aws_sdk_managedblockchain_query.types.contract_identifier.ContractIdentifier"
    """<p>The container for the contract identifier containing its blockchain network and address.</p>"""
    token_standard: "aws_sdk_managedblockchain_query.types.query_token_standard.QueryTokenStandard"
    """<p>The token standard of the contract.</p>"""
    deployer_address: "aws_sdk_managedblockchain_query.types.chain_address.ChainAddress"
    """<p>The address of the contract deployer.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AssetContract) -> dict:
    out: dict = {}
    import aws_sdk_managedblockchain_query.types.contract_identifier
    out["contractIdentifier"] = aws_sdk_managedblockchain_query.types.contract_identifier.serialize_json(value["contract_identifier"])
    out["tokenStandard"] = value["token_standard"]
    out["deployerAddress"] = value["deployer_address"]
    return out


def deserialize_json(data: dict) -> AssetContract:
    out: AssetContract = {}  # type: ignore[typeddict-item]
    if "contractIdentifier" in data:
        import aws_sdk_managedblockchain_query.types.contract_identifier
        out["contract_identifier"] = aws_sdk_managedblockchain_query.types.contract_identifier.deserialize_json(data["contractIdentifier"])
    else:
        raise DeserializationError("AssetContract.contract_identifier required")
    if "tokenStandard" in data:
        out["token_standard"] = data["tokenStandard"]
    else:
        raise DeserializationError("AssetContract.token_standard required")
    if "deployerAddress" in data:
        out["deployer_address"] = data["deployerAddress"]
    else:
        raise DeserializationError("AssetContract.deployer_address required")
    return out