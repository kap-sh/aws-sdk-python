"""Generated from Smithy shape ``com.amazonaws.managedblockchain#NodeFabricLogPublishingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.log_configurations


class NodeFabricLogPublishingConfiguration(TypedDict, closed=True):
    chaincode_logs: NotRequired[
        "aws_sdk_managedblockchain.types.log_configurations.LogConfigurations"
    ]
    """<p>Configuration properties for logging events associated with chaincode execution on a peer node. Chaincode logs contain the results of instantiating, invoking, and querying the chaincode. A peer can run multiple instances of chaincode. When enabled, a log stream is created for all chaincodes, with an individual log stream for each chaincode.</p>"""
    peer_logs: NotRequired[
        "aws_sdk_managedblockchain.types.log_configurations.LogConfigurations"
    ]
    """<p>Configuration properties for a peer node log. Peer node logs contain messages generated when your client submits transaction proposals to peer nodes, requests to join channels, enrolls an admin peer, and lists the chaincode instances on a peer node. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeFabricLogPublishingConfiguration) -> dict:
    out: dict = {}
    if "chaincode_logs" in value:
        import aws_sdk_managedblockchain.types.log_configurations

        out["ChaincodeLogs"] = (
            aws_sdk_managedblockchain.types.log_configurations.serialize_json(
                value["chaincode_logs"]
            )
        )
    if "peer_logs" in value:
        import aws_sdk_managedblockchain.types.log_configurations

        out["PeerLogs"] = (
            aws_sdk_managedblockchain.types.log_configurations.serialize_json(
                value["peer_logs"]
            )
        )
    return out


def deserialize_json(data: dict) -> NodeFabricLogPublishingConfiguration:
    out: NodeFabricLogPublishingConfiguration = {}  # type: ignore[typeddict-item]
    if "ChaincodeLogs" in data:
        import aws_sdk_managedblockchain.types.log_configurations

        out["chaincode_logs"] = (
            aws_sdk_managedblockchain.types.log_configurations.deserialize_json(
                data["ChaincodeLogs"]
            )
        )
    if "PeerLogs" in data:
        import aws_sdk_managedblockchain.types.log_configurations

        out["peer_logs"] = (
            aws_sdk_managedblockchain.types.log_configurations.deserialize_json(
                data["PeerLogs"]
            )
        )
    return out
