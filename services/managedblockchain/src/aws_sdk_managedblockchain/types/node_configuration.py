"""Generated from Smithy shape ``com.amazonaws.managedblockchain#NodeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_managedblockchain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.availability_zone_string
    import aws_sdk_managedblockchain.types.instance_type_string
    import aws_sdk_managedblockchain.types.node_log_publishing_configuration
    import aws_sdk_managedblockchain.types.state_db_type


class NodeConfiguration(TypedDict, closed=True):
    instance_type: (
        "aws_sdk_managedblockchain.types.instance_type_string.InstanceTypeString"
    )
    """<p>The Amazon Managed Blockchain instance type for the node.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_managedblockchain.types.availability_zone_string.AvailabilityZoneString"
    ]
    """<p>The Availability Zone in which the node exists. Required for Ethereum nodes. </p>"""
    log_publishing_configuration: NotRequired[
        "aws_sdk_managedblockchain.types.node_log_publishing_configuration.NodeLogPublishingConfiguration"
    ]
    """<p>Configuration properties for logging events associated with a peer node on a Hyperledger Fabric network on Managed Blockchain. </p>"""
    state_db: NotRequired["aws_sdk_managedblockchain.types.state_db_type.StateDBType"]
    """<p>The state database that the node uses. Values are <code>LevelDB</code> or <code>CouchDB</code>. When using an Amazon Managed Blockchain network with Hyperledger Fabric version 1.4 or later, the default is <code>CouchDB</code>.</p> <p>Applies only to Hyperledger Fabric.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeConfiguration) -> dict:
    out: dict = {}
    out["InstanceType"] = value["instance_type"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "log_publishing_configuration" in value:
        import aws_sdk_managedblockchain.types.node_log_publishing_configuration

        out["LogPublishingConfiguration"] = (
            aws_sdk_managedblockchain.types.node_log_publishing_configuration.serialize_json(
                value["log_publishing_configuration"]
            )
        )
    if "state_db" in value:
        import aws_sdk_managedblockchain.types.state_db_type

        out["StateDB"] = aws_sdk_managedblockchain.types.state_db_type.serialize_json(
            value["state_db"]
        )
    return out


def deserialize_json(data: dict) -> NodeConfiguration:
    out: NodeConfiguration = {}  # type: ignore[typeddict-item]
    if "InstanceType" in data:
        out["instance_type"] = data["InstanceType"]
    else:
        raise DeserializationError("NodeConfiguration.instance_type required")
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "LogPublishingConfiguration" in data:
        import aws_sdk_managedblockchain.types.node_log_publishing_configuration

        out["log_publishing_configuration"] = (
            aws_sdk_managedblockchain.types.node_log_publishing_configuration.deserialize_json(
                data["LogPublishingConfiguration"]
            )
        )
    if "StateDB" in data:
        import aws_sdk_managedblockchain.types.state_db_type

        out["state_db"] = (
            aws_sdk_managedblockchain.types.state_db_type.deserialize_json(
                data["StateDB"]
            )
        )
    return out
