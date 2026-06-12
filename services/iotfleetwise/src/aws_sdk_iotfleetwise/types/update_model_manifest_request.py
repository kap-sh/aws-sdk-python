"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#UpdateModelManifestRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.description
    import aws_sdk_iotfleetwise.types.manifest_status
    import aws_sdk_iotfleetwise.types.node_paths
    import aws_sdk_iotfleetwise.types.resource_name


class UpdateModelManifestRequest(TypedDict):
    name: "aws_sdk_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the vehicle model to update. </p>"""
    description: NotRequired["aws_sdk_iotfleetwise.types.description.description"]
    """<p> A brief description of the vehicle model. </p>"""
    nodes_to_add: NotRequired["aws_sdk_iotfleetwise.types.node_paths.NodePaths"]
    """<p> A list of <code>fullyQualifiedName</code> of nodes, which are a general abstraction of signals, to add to the vehicle model. </p>"""
    nodes_to_remove: NotRequired["aws_sdk_iotfleetwise.types.node_paths.NodePaths"]
    """<p> A list of <code>fullyQualifiedName</code> of nodes, which are a general abstraction of signals, to remove from the vehicle model. </p>"""
    status: NotRequired["aws_sdk_iotfleetwise.types.manifest_status.ManifestStatus"]
    """<p> The state of the vehicle model. If the status is <code>ACTIVE</code>, the vehicle model can't be edited. If the status is <code>DRAFT</code>, you can edit the vehicle model. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateModelManifestRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "nodes_to_add" in value:
        import aws_sdk_iotfleetwise.types.node_paths

        out["nodesToAdd"] = (
            aws_sdk_iotfleetwise.types.node_paths.serialize_aws_json_1_0(
                value["nodes_to_add"]
            )
        )
    if "nodes_to_remove" in value:
        import aws_sdk_iotfleetwise.types.node_paths

        out["nodesToRemove"] = (
            aws_sdk_iotfleetwise.types.node_paths.serialize_aws_json_1_0(
                value["nodes_to_remove"]
            )
        )
    if "status" in value:
        import aws_sdk_iotfleetwise.types.manifest_status

        out["status"] = (
            aws_sdk_iotfleetwise.types.manifest_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateModelManifestRequest:
    out: UpdateModelManifestRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "nodesToAdd" in data:
        import aws_sdk_iotfleetwise.types.node_paths

        out["nodes_to_add"] = (
            aws_sdk_iotfleetwise.types.node_paths.deserialize_aws_json_1_0(
                data["nodesToAdd"]
            )
        )
    if "nodesToRemove" in data:
        import aws_sdk_iotfleetwise.types.node_paths

        out["nodes_to_remove"] = (
            aws_sdk_iotfleetwise.types.node_paths.deserialize_aws_json_1_0(
                data["nodesToRemove"]
            )
        )
    if "status" in data:
        import aws_sdk_iotfleetwise.types.manifest_status

        out["status"] = (
            aws_sdk_iotfleetwise.types.manifest_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    return out
