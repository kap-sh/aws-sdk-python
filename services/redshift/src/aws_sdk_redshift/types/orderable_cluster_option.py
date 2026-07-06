"""Generated from Smithy shape ``com.amazonaws.redshift#OrderableClusterOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.availability_zone_list
    import aws_sdk_redshift.types.string


class OrderableClusterOption(TypedDict, closed=True):
    cluster_version: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The version of the orderable cluster.</p>"""
    cluster_type: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The cluster type, for example <code>multi-node</code>. </p>"""
    node_type: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The node type for the orderable cluster.</p>"""
    availability_zones: NotRequired[
        "aws_sdk_redshift.types.availability_zone_list.AvailabilityZoneList"
    ]
    """<p>A list of availability zones for the orderable cluster.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OrderableClusterOption, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_version" in value:
        pairs.append((f"{prefix}.ClusterVersion", str(value["cluster_version"])))
    if "cluster_type" in value:
        pairs.append((f"{prefix}.ClusterType", str(value["cluster_type"])))
    if "node_type" in value:
        pairs.append((f"{prefix}.NodeType", str(value["node_type"])))
    if "availability_zones" in value:
        import aws_sdk_redshift.types.availability_zone_list

        aws_sdk_redshift.types.availability_zone_list.serialize_query(
            value["availability_zones"], pairs, f"{prefix}.AvailabilityZones"
        )


def deserialize_query(el: Element) -> OrderableClusterOption:
    out: OrderableClusterOption = {}  # type: ignore[typeddict-item]
    child_cluster_version = el.find("ClusterVersion")
    if child_cluster_version is not None:
        out["cluster_version"] = str(child_cluster_version.text or "")
    child_cluster_type = el.find("ClusterType")
    if child_cluster_type is not None:
        out["cluster_type"] = str(child_cluster_type.text or "")
    child_node_type = el.find("NodeType")
    if child_node_type is not None:
        out["node_type"] = str(child_node_type.text or "")
    child_availability_zones = el.find("AvailabilityZones")
    if child_availability_zones is not None:
        import aws_sdk_redshift.types.availability_zone_list

        out["availability_zones"] = (
            aws_sdk_redshift.types.availability_zone_list.deserialize_query(
                child_availability_zones
            )
        )
    return out
