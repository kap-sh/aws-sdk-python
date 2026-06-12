"""Generated from Smithy shape ``com.amazonaws.managedblockchain#NetworkFrameworkAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.network_ethereum_attributes
    import aws_sdk_managedblockchain.types.network_fabric_attributes


class NetworkFrameworkAttributes(TypedDict):
    fabric: NotRequired[
        "aws_sdk_managedblockchain.types.network_fabric_attributes.NetworkFabricAttributes"
    ]
    """<p>Attributes of Hyperledger Fabric for a Managed Blockchain network that uses Hyperledger Fabric.</p>"""
    ethereum: NotRequired[
        "aws_sdk_managedblockchain.types.network_ethereum_attributes.NetworkEthereumAttributes"
    ]
    """<p>Attributes of an Ethereum network for Managed Blockchain resources participating in an Ethereum network. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkFrameworkAttributes) -> dict:
    out: dict = {}
    if "fabric" in value:
        import aws_sdk_managedblockchain.types.network_fabric_attributes

        out["Fabric"] = (
            aws_sdk_managedblockchain.types.network_fabric_attributes.serialize_json(
                value["fabric"]
            )
        )
    if "ethereum" in value:
        import aws_sdk_managedblockchain.types.network_ethereum_attributes

        out["Ethereum"] = (
            aws_sdk_managedblockchain.types.network_ethereum_attributes.serialize_json(
                value["ethereum"]
            )
        )
    return out


def deserialize_json(data: dict) -> NetworkFrameworkAttributes:
    out: NetworkFrameworkAttributes = {}  # type: ignore[typeddict-item]
    if "Fabric" in data:
        import aws_sdk_managedblockchain.types.network_fabric_attributes

        out["fabric"] = (
            aws_sdk_managedblockchain.types.network_fabric_attributes.deserialize_json(
                data["Fabric"]
            )
        )
    if "Ethereum" in data:
        import aws_sdk_managedblockchain.types.network_ethereum_attributes

        out["ethereum"] = (
            aws_sdk_managedblockchain.types.network_ethereum_attributes.deserialize_json(
                data["Ethereum"]
            )
        )
    return out
