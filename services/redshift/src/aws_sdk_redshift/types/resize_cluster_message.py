"""Generated from Smithy shape ``com.amazonaws.redshift#ResizeClusterMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.boolean_optional
    import aws_sdk_redshift.types.integer_optional
    import aws_sdk_redshift.types.string


class ResizeClusterMessage(TypedDict):
    cluster_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The unique identifier for the cluster to resize.</p>"""
    cluster_type: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The new cluster type for the specified cluster.</p>"""
    node_type: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The new node type for the nodes you are adding. If not specified, the cluster's current node type is used.</p>"""
    number_of_nodes: NotRequired[
        "aws_sdk_redshift.types.integer_optional.IntegerOptional"
    ]
    """<p>The new number of nodes for the cluster. If not specified, the cluster's current number of nodes is used.</p>"""
    classic: NotRequired["aws_sdk_redshift.types.boolean_optional.BooleanOptional"]
    """<p>A boolean value indicating whether the resize operation is using the classic resize process. If you don't provide this parameter or set the value to <code>false</code>, the resize type is elastic. </p>"""
    reserved_node_id: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The identifier of the reserved node.</p>"""
    target_reserved_node_offering_id: NotRequired[
        "aws_sdk_redshift.types.string.String"
    ]
    """<p>The identifier of the target reserved node offering.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResizeClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))
    if "cluster_type" in value:
        pairs.append((f"{prefix}.ClusterType", str(value["cluster_type"])))
    if "node_type" in value:
        pairs.append((f"{prefix}.NodeType", str(value["node_type"])))
    if "number_of_nodes" in value:
        pairs.append((f"{prefix}.NumberOfNodes", str(value["number_of_nodes"])))
    if "classic" in value:
        pairs.append((f"{prefix}.Classic", "true" if value["classic"] else "false"))
    if "reserved_node_id" in value:
        pairs.append((f"{prefix}.ReservedNodeId", str(value["reserved_node_id"])))
    if "target_reserved_node_offering_id" in value:
        pairs.append(
            (
                f"{prefix}.TargetReservedNodeOfferingId",
                str(value["target_reserved_node_offering_id"]),
            )
        )


def deserialize_query(el: Element) -> ResizeClusterMessage:
    out: ResizeClusterMessage = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_cluster_type = el.find("ClusterType")
    if child_cluster_type is not None:
        out["cluster_type"] = str(child_cluster_type.text or "")
    child_node_type = el.find("NodeType")
    if child_node_type is not None:
        out["node_type"] = str(child_node_type.text or "")
    child_number_of_nodes = el.find("NumberOfNodes")
    if child_number_of_nodes is not None:
        out["number_of_nodes"] = int(child_number_of_nodes.text or "")
    child_classic = el.find("Classic")
    if child_classic is not None:
        out["classic"] = (child_classic.text or "").lower() == "true"
    child_reserved_node_id = el.find("ReservedNodeId")
    if child_reserved_node_id is not None:
        out["reserved_node_id"] = str(child_reserved_node_id.text or "")
    child_target_reserved_node_offering_id = el.find("TargetReservedNodeOfferingId")
    if child_target_reserved_node_offering_id is not None:
        out["target_reserved_node_offering_id"] = str(
            child_target_reserved_node_offering_id.text or ""
        )
    return out
