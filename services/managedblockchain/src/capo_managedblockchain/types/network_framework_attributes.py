"""Generated from Smithy shape ``com.amazonaws.managedblockchain#NetworkFrameworkAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.network_ethereum_attributes
    import capo_managedblockchain.types.network_fabric_attributes


class NetworkFrameworkAttributes(TypedDict, closed=True):
    fabric: NotRequired[
        "capo_managedblockchain.types.network_fabric_attributes.NetworkFabricAttributes"
    ]
    """<p>Attributes of Hyperledger Fabric for a Managed Blockchain network that uses Hyperledger Fabric.</p>"""
    ethereum: NotRequired[
        "capo_managedblockchain.types.network_ethereum_attributes.NetworkEthereumAttributes"
    ]
    """<p>Attributes of an Ethereum network for Managed Blockchain resources participating in an Ethereum network. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkFrameworkAttributes) -> dict:
    out: dict = {}
    if "fabric" in value:
        import capo_managedblockchain.types.network_fabric_attributes

        out["Fabric"] = (
            capo_managedblockchain.types.network_fabric_attributes.serialize_json(
                value["fabric"]
            )
        )
    if "ethereum" in value:
        import capo_managedblockchain.types.network_ethereum_attributes

        out["Ethereum"] = (
            capo_managedblockchain.types.network_ethereum_attributes.serialize_json(
                value["ethereum"]
            )
        )
    return out


def deserialize_json(data: dict) -> NetworkFrameworkAttributes:
    out: NetworkFrameworkAttributes = {}  # type: ignore[typeddict-item]
    if "Fabric" in data:
        import capo_managedblockchain.types.network_fabric_attributes

        out["fabric"] = (
            capo_managedblockchain.types.network_fabric_attributes.deserialize_json(
                data["Fabric"]
            )
        )
    if "Ethereum" in data:
        import capo_managedblockchain.types.network_ethereum_attributes

        out["ethereum"] = (
            capo_managedblockchain.types.network_ethereum_attributes.deserialize_json(
                data["Ethereum"]
            )
        )
    return out
