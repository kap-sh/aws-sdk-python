"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeOrderableClusterOptionsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.integer_optional
    import aws_sdk_redshift.types.string


class DescribeOrderableClusterOptionsMessage(TypedDict, closed=True):
    cluster_version: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The version filter value. Specify this parameter to show only the available offerings matching the specified version.</p> <p>Default: All versions.</p> <p>Constraints: Must be one of the version returned from <a>DescribeClusterVersions</a>.</p>"""
    node_type: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The node type filter value. Specify this parameter to show only the available offerings matching the specified node type.</p>"""
    max_records: NotRequired["aws_sdk_redshift.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>"""
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeOrderableClusterOptions</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeOrderableClusterOptionsMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "cluster_version" in value:
        pairs.append((f"{prefix}.ClusterVersion", str(value["cluster_version"])))
    if "node_type" in value:
        pairs.append((f"{prefix}.NodeType", str(value["node_type"])))
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeOrderableClusterOptionsMessage:
    out: DescribeOrderableClusterOptionsMessage = {}  # type: ignore[typeddict-item]
    child_cluster_version = el.find("ClusterVersion")
    if child_cluster_version is not None:
        out["cluster_version"] = str(child_cluster_version.text or "")
    child_node_type = el.find("NodeType")
    if child_node_type is not None:
        out["node_type"] = str(child_node_type.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
