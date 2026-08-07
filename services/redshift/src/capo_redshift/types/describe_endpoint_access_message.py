"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeEndpointAccessMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.integer_optional
    import capo_redshift.types.string


class DescribeEndpointAccessMessage(TypedDict, closed=True):
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The cluster identifier associated with the described endpoint.</p>"""
    resource_owner: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the cluster.</p>"""
    endpoint_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the endpoint to be described.</p>"""
    vpc_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The virtual private cloud (VPC) identifier with access to the cluster.</p>"""
    max_records: NotRequired["capo_redshift.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a <code>Marker</code> is included in the response so that the remaining results can be retrieved.</p>"""
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeEndpointAccess</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the <code>MaxRecords</code> parameter.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeEndpointAccessMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}ClusterIdentifier", str(value["cluster_identifier"]))
        )
    if "resource_owner" in value:
        pairs.append((f"{key_prefix}ResourceOwner", str(value["resource_owner"])))
    if "endpoint_name" in value:
        pairs.append((f"{key_prefix}EndpointName", str(value["endpoint_name"])))
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeEndpointAccessMessage:
    out: DescribeEndpointAccessMessage = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_resource_owner = el.find("ResourceOwner")
    if child_resource_owner is not None:
        out["resource_owner"] = str(child_resource_owner.text or "")
    child_endpoint_name = el.find("EndpointName")
    if child_endpoint_name is not None:
        out["endpoint_name"] = str(child_endpoint_name.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
