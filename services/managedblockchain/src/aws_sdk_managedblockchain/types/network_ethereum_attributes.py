"""Generated from Smithy shape ``com.amazonaws.managedblockchain#NetworkEthereumAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.string


class NetworkEthereumAttributes(TypedDict, closed=True):
    chain_id: NotRequired["aws_sdk_managedblockchain.types.string.String"]
    """<p>The Ethereum <code>CHAIN_ID</code> associated with the Ethereum network. Chain IDs are as follows:</p> <ul> <li> <p>mainnet = <code>1</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkEthereumAttributes) -> dict:
    out: dict = {}
    if "chain_id" in value:
        out["ChainId"] = value["chain_id"]
    return out


def deserialize_json(data: dict) -> NetworkEthereumAttributes:
    out: NetworkEthereumAttributes = {}  # type: ignore[typeddict-item]
    if "ChainId" in data:
        out["chain_id"] = data["ChainId"]
    return out
