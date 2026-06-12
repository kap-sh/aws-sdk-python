"""Generated from Smithy shape ``com.amazonaws.managedblockchain#NodeFrameworkAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.node_ethereum_attributes
    import aws_sdk_managedblockchain.types.node_fabric_attributes


class NodeFrameworkAttributes(TypedDict):
    fabric: NotRequired[
        "aws_sdk_managedblockchain.types.node_fabric_attributes.NodeFabricAttributes"
    ]
    """<p>Attributes of Hyperledger Fabric for a peer node on a Managed Blockchain network that uses Hyperledger Fabric.</p>"""
    ethereum: NotRequired[
        "aws_sdk_managedblockchain.types.node_ethereum_attributes.NodeEthereumAttributes"
    ]
    """<p>Attributes of Ethereum for a node on a Managed Blockchain network that uses Ethereum. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeFrameworkAttributes) -> dict:
    out: dict = {}
    if "fabric" in value:
        import aws_sdk_managedblockchain.types.node_fabric_attributes

        out["Fabric"] = (
            aws_sdk_managedblockchain.types.node_fabric_attributes.serialize_json(
                value["fabric"]
            )
        )
    if "ethereum" in value:
        import aws_sdk_managedblockchain.types.node_ethereum_attributes

        out["Ethereum"] = (
            aws_sdk_managedblockchain.types.node_ethereum_attributes.serialize_json(
                value["ethereum"]
            )
        )
    return out


def deserialize_json(data: dict) -> NodeFrameworkAttributes:
    out: NodeFrameworkAttributes = {}  # type: ignore[typeddict-item]
    if "Fabric" in data:
        import aws_sdk_managedblockchain.types.node_fabric_attributes

        out["fabric"] = (
            aws_sdk_managedblockchain.types.node_fabric_attributes.deserialize_json(
                data["Fabric"]
            )
        )
    if "Ethereum" in data:
        import aws_sdk_managedblockchain.types.node_ethereum_attributes

        out["ethereum"] = (
            aws_sdk_managedblockchain.types.node_ethereum_attributes.deserialize_json(
                data["Ethereum"]
            )
        )
    return out
