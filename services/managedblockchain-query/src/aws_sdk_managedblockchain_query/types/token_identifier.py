"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#TokenIdentifier``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.chain_address
    import aws_sdk_managedblockchain_query.types.query_network
    import aws_sdk_managedblockchain_query.types.query_token_id


class TokenIdentifier(TypedDict):
    network: "aws_sdk_managedblockchain_query.types.query_network.QueryNetwork"
    """<p>The blockchain network of the token.</p>"""
    contract_address: NotRequired[
        "aws_sdk_managedblockchain_query.types.chain_address.ChainAddress"
    ]
    """<p>This is the token's contract address.</p>"""
    token_id: NotRequired[
        "aws_sdk_managedblockchain_query.types.query_token_id.QueryTokenId"
    ]
    """<p>The unique identifier of the token.</p> <note> <p>For native tokens, use the 3 character abbreviation that best matches your token. For example, btc for Bitcoin, eth for Ether, etc. For all other token types you must specify the <code>tokenId</code> in the 64 character hexadecimal <code>tokenid</code> format.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: TokenIdentifier) -> dict:
    out: dict = {}
    out["network"] = value["network"]
    if "contract_address" in value:
        out["contractAddress"] = value["contract_address"]
    if "token_id" in value:
        out["tokenId"] = value["token_id"]
    return out


def deserialize_json(data: dict) -> TokenIdentifier:
    out: TokenIdentifier = {}  # type: ignore[typeddict-item]
    if "network" in data:
        out["network"] = data["network"]
    else:
        raise DeserializationError("TokenIdentifier.network required")
    if "contractAddress" in data:
        out["contract_address"] = data["contractAddress"]
    if "tokenId" in data:
        out["token_id"] = data["tokenId"]
    return out
