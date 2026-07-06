"""Generated from Smithy shape ``com.amazonaws.redshift#SecondaryClusterInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.cluster_nodes_list
    import aws_sdk_redshift.types.string


class SecondaryClusterInfo(TypedDict, closed=True):
    availability_zone: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The name of the Availability Zone in which the secondary compute unit of the cluster is located.</p>"""
    cluster_nodes: NotRequired[
        "aws_sdk_redshift.types.cluster_nodes_list.ClusterNodesList"
    ]
    """<p>The nodes in the secondary compute unit.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SecondaryClusterInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "cluster_nodes" in value:
        import aws_sdk_redshift.types.cluster_nodes_list

        aws_sdk_redshift.types.cluster_nodes_list.serialize_query(
            value["cluster_nodes"], pairs, f"{prefix}.ClusterNodes"
        )


def deserialize_query(el: Element) -> SecondaryClusterInfo:
    out: SecondaryClusterInfo = {}  # type: ignore[typeddict-item]
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_cluster_nodes = el.find("ClusterNodes")
    if child_cluster_nodes is not None:
        import aws_sdk_redshift.types.cluster_nodes_list

        out["cluster_nodes"] = (
            aws_sdk_redshift.types.cluster_nodes_list.deserialize_query(
                child_cluster_nodes
            )
        )
    return out
