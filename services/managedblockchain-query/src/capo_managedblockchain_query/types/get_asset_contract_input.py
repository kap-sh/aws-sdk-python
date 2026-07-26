"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#GetAssetContractInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.contract_identifier


class GetAssetContractInput(TypedDict, closed=True):
    contract_identifier: (
        "capo_managedblockchain_query.types.contract_identifier.ContractIdentifier"
    )
    """<p>Contains the blockchain address and network information about the contract.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssetContractInput) -> dict:
    out: dict = {}
    import capo_managedblockchain_query.types.contract_identifier

    out["contractIdentifier"] = (
        capo_managedblockchain_query.types.contract_identifier.serialize_json(
            value["contract_identifier"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetAssetContractInput:
    out: GetAssetContractInput = {}  # type: ignore[typeddict-item]
    if "contractIdentifier" in data:
        import capo_managedblockchain_query.types.contract_identifier

        out["contract_identifier"] = (
            capo_managedblockchain_query.types.contract_identifier.deserialize_json(
                data["contractIdentifier"]
            )
        )
    else:
        raise DeserializationError("GetAssetContractInput.contract_identifier required")
    return out
