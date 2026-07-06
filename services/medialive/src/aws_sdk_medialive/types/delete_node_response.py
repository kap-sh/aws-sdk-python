"""Generated from Smithy shape ``com.amazonaws.medialive#DeleteNodeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of__string
    import aws_sdk_medialive.types.__list_of_node_interface_mapping
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.node_connection_state
    import aws_sdk_medialive.types.node_role
    import aws_sdk_medialive.types.node_state
    import aws_sdk_medialive.types.sdi_source_mappings


class DeleteNodeResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ARN of the Node. It is automatically assigned when the Node is created."""
    channel_placement_groups: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """An array of IDs. Each ID is one ChannelPlacementGroup that is associated with this Node. Empty if the Node is not yet associated with any groups."""
    cluster_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ID of the Cluster that the Node belongs to."""
    connection_state: NotRequired[
        "aws_sdk_medialive.types.node_connection_state.NodeConnectionState"
    ]
    """The current connection state of the Node."""
    id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The unique ID of the Node. Unique in the Cluster. The ID is the resource-id portion of the ARN."""
    instance_arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ARN of the EC2 instance hosting the Node."""
    name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The name that you specified for the Node."""
    node_interface_mappings: NotRequired[
        "aws_sdk_medialive.types.__list_of_node_interface_mapping.__listOfNodeInterfaceMapping"
    ]
    """Documentation update needed"""
    role: NotRequired["aws_sdk_medialive.types.node_role.NodeRole"]
    """The initial role current role of the Node in the Cluster. ACTIVE means the Node is available for encoding. BACKUP means the Node is a redundant Node and might get used if an ACTIVE Node fails."""
    state: NotRequired["aws_sdk_medialive.types.node_state.NodeState"]
    """The current state of the Node."""
    sdi_source_mappings: NotRequired[
        "aws_sdk_medialive.types.sdi_source_mappings.SdiSourceMappings"
    ]
    """An array of SDI source mappings. Each mapping connects one logical SdiSource to the physical SDI card and port that the physical SDI source uses."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteNodeResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "channel_placement_groups" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["channelPlacementGroups"] = (
            aws_sdk_medialive.types.__list_of__string.serialize_json(
                value["channel_placement_groups"]
            )
        )
    if "cluster_id" in value:
        out["clusterId"] = value["cluster_id"]
    if "connection_state" in value:
        import aws_sdk_medialive.types.node_connection_state

        out["connectionState"] = (
            aws_sdk_medialive.types.node_connection_state.serialize_json(
                value["connection_state"]
            )
        )
    if "id" in value:
        out["id"] = value["id"]
    if "instance_arn" in value:
        out["instanceArn"] = value["instance_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "node_interface_mappings" in value:
        import aws_sdk_medialive.types.__list_of_node_interface_mapping

        out["nodeInterfaceMappings"] = (
            aws_sdk_medialive.types.__list_of_node_interface_mapping.serialize_json(
                value["node_interface_mappings"]
            )
        )
    if "role" in value:
        import aws_sdk_medialive.types.node_role

        out["role"] = aws_sdk_medialive.types.node_role.serialize_json(value["role"])
    if "state" in value:
        import aws_sdk_medialive.types.node_state

        out["state"] = aws_sdk_medialive.types.node_state.serialize_json(value["state"])
    if "sdi_source_mappings" in value:
        import aws_sdk_medialive.types.sdi_source_mappings

        out["sdiSourceMappings"] = (
            aws_sdk_medialive.types.sdi_source_mappings.serialize_json(
                value["sdi_source_mappings"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteNodeResponse:
    out: DeleteNodeResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "channelPlacementGroups" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["channel_placement_groups"] = (
            aws_sdk_medialive.types.__list_of__string.deserialize_json(
                data["channelPlacementGroups"]
            )
        )
    if "clusterId" in data:
        out["cluster_id"] = data["clusterId"]
    if "connectionState" in data:
        import aws_sdk_medialive.types.node_connection_state

        out["connection_state"] = (
            aws_sdk_medialive.types.node_connection_state.deserialize_json(
                data["connectionState"]
            )
        )
    if "id" in data:
        out["id"] = data["id"]
    if "instanceArn" in data:
        out["instance_arn"] = data["instanceArn"]
    if "name" in data:
        out["name"] = data["name"]
    if "nodeInterfaceMappings" in data:
        import aws_sdk_medialive.types.__list_of_node_interface_mapping

        out["node_interface_mappings"] = (
            aws_sdk_medialive.types.__list_of_node_interface_mapping.deserialize_json(
                data["nodeInterfaceMappings"]
            )
        )
    if "role" in data:
        import aws_sdk_medialive.types.node_role

        out["role"] = aws_sdk_medialive.types.node_role.deserialize_json(data["role"])
    if "state" in data:
        import aws_sdk_medialive.types.node_state

        out["state"] = aws_sdk_medialive.types.node_state.deserialize_json(
            data["state"]
        )
    if "sdiSourceMappings" in data:
        import aws_sdk_medialive.types.sdi_source_mappings

        out["sdi_source_mappings"] = (
            aws_sdk_medialive.types.sdi_source_mappings.deserialize_json(
                data["sdiSourceMappings"]
            )
        )
    return out
