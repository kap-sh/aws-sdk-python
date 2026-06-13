"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#ListAssetContractsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.asset_contract_list
    import aws_sdk_managedblockchain_query.types.next_token


class ListAssetContractsOutput(TypedDict):
    contracts: (
        "aws_sdk_managedblockchain_query.types.asset_contract_list.AssetContractList"
    )
    """<p>An array of contract objects that contain the properties for each contract.</p>"""
    next_token: NotRequired[
        "aws_sdk_managedblockchain_query.types.next_token.NextToken"
    ]
    """<p>The pagination token that indicates the next set of results to retrieve. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetContractsOutput) -> dict:
    out: dict = {}
    import aws_sdk_managedblockchain_query.types.asset_contract_list

    out["contracts"] = (
        aws_sdk_managedblockchain_query.types.asset_contract_list.serialize_json(
            value["contracts"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssetContractsOutput:
    out: ListAssetContractsOutput = {}  # type: ignore[typeddict-item]
    if "contracts" in data:
        import aws_sdk_managedblockchain_query.types.asset_contract_list

        out["contracts"] = (
            aws_sdk_managedblockchain_query.types.asset_contract_list.deserialize_json(
                data["contracts"]
            )
        )
    else:
        raise DeserializationError("ListAssetContractsOutput.contracts required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
