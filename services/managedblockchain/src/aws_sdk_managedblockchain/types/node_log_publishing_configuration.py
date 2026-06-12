"""Generated from Smithy shape ``com.amazonaws.managedblockchain#NodeLogPublishingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.node_fabric_log_publishing_configuration


class NodeLogPublishingConfiguration(TypedDict):
    fabric: NotRequired[
        "aws_sdk_managedblockchain.types.node_fabric_log_publishing_configuration.NodeFabricLogPublishingConfiguration"
    ]
    """<p>Configuration properties for logging events associated with a node that is owned by a member of a Managed Blockchain network using the Hyperledger Fabric framework.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeLogPublishingConfiguration) -> dict:
    out: dict = {}
    if "fabric" in value:
        import aws_sdk_managedblockchain.types.node_fabric_log_publishing_configuration

        out["Fabric"] = (
            aws_sdk_managedblockchain.types.node_fabric_log_publishing_configuration.serialize_json(
                value["fabric"]
            )
        )
    return out


def deserialize_json(data: dict) -> NodeLogPublishingConfiguration:
    out: NodeLogPublishingConfiguration = {}  # type: ignore[typeddict-item]
    if "Fabric" in data:
        import aws_sdk_managedblockchain.types.node_fabric_log_publishing_configuration

        out["fabric"] = (
            aws_sdk_managedblockchain.types.node_fabric_log_publishing_configuration.deserialize_json(
                data["Fabric"]
            )
        )
    return out
