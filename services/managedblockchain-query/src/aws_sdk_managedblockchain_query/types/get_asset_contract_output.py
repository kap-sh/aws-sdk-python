"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#GetAssetContractOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.chain_address
    import aws_sdk_managedblockchain_query.types.contract_identifier
    import aws_sdk_managedblockchain_query.types.contract_metadata
    import aws_sdk_managedblockchain_query.types.query_token_standard


class GetAssetContractOutput(TypedDict):
    contract_identifier: (
        "aws_sdk_managedblockchain_query.types.contract_identifier.ContractIdentifier"
    )
    """<p>Contains the blockchain address and network information about the contract.</p>"""
    token_standard: (
        "aws_sdk_managedblockchain_query.types.query_token_standard.QueryTokenStandard"
    )
    """<p>The token standard of the contract requested.</p>"""
    deployer_address: "aws_sdk_managedblockchain_query.types.chain_address.ChainAddress"
    """<p>The address of the deployer of contract.</p>"""
    metadata: NotRequired[
        "aws_sdk_managedblockchain_query.types.contract_metadata.ContractMetadata"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetAssetContractOutput) -> dict:
    out: dict = {}
    import aws_sdk_managedblockchain_query.types.contract_identifier

    out["contractIdentifier"] = (
        aws_sdk_managedblockchain_query.types.contract_identifier.serialize_json(
            value["contract_identifier"]
        )
    )
    out["tokenStandard"] = value["token_standard"]
    out["deployerAddress"] = value["deployer_address"]
    if "metadata" in value:
        import aws_sdk_managedblockchain_query.types.contract_metadata

        out["metadata"] = (
            aws_sdk_managedblockchain_query.types.contract_metadata.serialize_json(
                value["metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetAssetContractOutput:
    out: GetAssetContractOutput = {}  # type: ignore[typeddict-item]
    if "contractIdentifier" in data:
        import aws_sdk_managedblockchain_query.types.contract_identifier

        out["contract_identifier"] = (
            aws_sdk_managedblockchain_query.types.contract_identifier.deserialize_json(
                data["contractIdentifier"]
            )
        )
    else:
        raise DeserializationError(
            "GetAssetContractOutput.contract_identifier required"
        )
    if "tokenStandard" in data:
        out["token_standard"] = data["tokenStandard"]
    else:
        raise DeserializationError("GetAssetContractOutput.token_standard required")
    if "deployerAddress" in data:
        out["deployer_address"] = data["deployerAddress"]
    else:
        raise DeserializationError("GetAssetContractOutput.deployer_address required")
    if "metadata" in data:
        import aws_sdk_managedblockchain_query.types.contract_metadata

        out["metadata"] = (
            aws_sdk_managedblockchain_query.types.contract_metadata.deserialize_json(
                data["metadata"]
            )
        )
    return out
