"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#TokenFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.chain_address
    import aws_sdk_managedblockchain_query.types.query_network
    import aws_sdk_managedblockchain_query.types.query_token_id


class TokenFilter(TypedDict, closed=True):
    network: "aws_sdk_managedblockchain_query.types.query_network.QueryNetwork"
    """<p>The blockchain network of the token.</p>"""
    contract_address: NotRequired[
        "aws_sdk_managedblockchain_query.types.chain_address.ChainAddress"
    ]
    """<p>This is the address of the contract.</p>"""
    token_id: NotRequired[
        "aws_sdk_managedblockchain_query.types.query_token_id.QueryTokenId"
    ]
    """<p>The unique identifier of the token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TokenFilter) -> dict:
    out: dict = {}
    out["network"] = value["network"]
    if "contract_address" in value:
        out["contractAddress"] = value["contract_address"]
    if "token_id" in value:
        out["tokenId"] = value["token_id"]
    return out


def deserialize_json(data: dict) -> TokenFilter:
    out: TokenFilter = {}  # type: ignore[typeddict-item]
    if "network" in data:
        out["network"] = data["network"]
    else:
        raise DeserializationError("TokenFilter.network required")
    if "contractAddress" in data:
        out["contract_address"] = data["contractAddress"]
    if "tokenId" in data:
        out["token_id"] = data["tokenId"]
    return out
