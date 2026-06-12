"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#UpdateSignalCatalogRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.description
    import aws_sdk_iotfleetwise.types.node_paths
    import aws_sdk_iotfleetwise.types.nodes
    import aws_sdk_iotfleetwise.types.resource_name


class UpdateSignalCatalogRequest(TypedDict):
    name: "aws_sdk_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the signal catalog to update. </p>"""
    description: NotRequired["aws_sdk_iotfleetwise.types.description.description"]
    """<p> A brief description of the signal catalog to update.</p>"""
    nodes_to_add: NotRequired["aws_sdk_iotfleetwise.types.nodes.Nodes"]
    """<p> A list of information about nodes to add to the signal catalog. </p>"""
    nodes_to_update: NotRequired["aws_sdk_iotfleetwise.types.nodes.Nodes"]
    """<p> A list of information about nodes to update in the signal catalog. </p>"""
    nodes_to_remove: NotRequired["aws_sdk_iotfleetwise.types.node_paths.NodePaths"]
    """<p> A list of <code>fullyQualifiedName</code> of nodes to remove from the signal catalog. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateSignalCatalogRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "nodes_to_add" in value:
        import aws_sdk_iotfleetwise.types.nodes

        out["nodesToAdd"] = aws_sdk_iotfleetwise.types.nodes.serialize_aws_json_1_0(
            value["nodes_to_add"]
        )
    if "nodes_to_update" in value:
        import aws_sdk_iotfleetwise.types.nodes

        out["nodesToUpdate"] = aws_sdk_iotfleetwise.types.nodes.serialize_aws_json_1_0(
            value["nodes_to_update"]
        )
    if "nodes_to_remove" in value:
        import aws_sdk_iotfleetwise.types.node_paths

        out["nodesToRemove"] = (
            aws_sdk_iotfleetwise.types.node_paths.serialize_aws_json_1_0(
                value["nodes_to_remove"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateSignalCatalogRequest:
    out: UpdateSignalCatalogRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "nodesToAdd" in data:
        import aws_sdk_iotfleetwise.types.nodes

        out["nodes_to_add"] = aws_sdk_iotfleetwise.types.nodes.deserialize_aws_json_1_0(
            data["nodesToAdd"]
        )
    if "nodesToUpdate" in data:
        import aws_sdk_iotfleetwise.types.nodes

        out["nodes_to_update"] = (
            aws_sdk_iotfleetwise.types.nodes.deserialize_aws_json_1_0(
                data["nodesToUpdate"]
            )
        )
    if "nodesToRemove" in data:
        import aws_sdk_iotfleetwise.types.node_paths

        out["nodes_to_remove"] = (
            aws_sdk_iotfleetwise.types.node_paths.deserialize_aws_json_1_0(
                data["nodesToRemove"]
            )
        )
    return out
