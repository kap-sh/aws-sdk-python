"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterEndpointMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_cluster_endpoint_list
    import aws_sdk_rds.types.string


class DBClusterEndpointMessage(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeDBClusterEndpoints</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    db_cluster_endpoints: NotRequired[
        "aws_sdk_rds.types.db_cluster_endpoint_list.DBClusterEndpointList"
    ]
    """<p>Contains the details of the endpoints associated with the cluster and matching any filter conditions.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterEndpointMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "db_cluster_endpoints" in value:
        import aws_sdk_rds.types.db_cluster_endpoint_list

        aws_sdk_rds.types.db_cluster_endpoint_list.serialize_query(
            value["db_cluster_endpoints"], pairs, f"{prefix}.DBClusterEndpoints"
        )


def deserialize_query(el: Element) -> DBClusterEndpointMessage:
    out: DBClusterEndpointMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_db_cluster_endpoints = el.find("DBClusterEndpoints")
    if child_db_cluster_endpoints is not None:
        import aws_sdk_rds.types.db_cluster_endpoint_list

        out["db_cluster_endpoints"] = (
            aws_sdk_rds.types.db_cluster_endpoint_list.deserialize_query(
                child_db_cluster_endpoints
            )
        )
    return out
