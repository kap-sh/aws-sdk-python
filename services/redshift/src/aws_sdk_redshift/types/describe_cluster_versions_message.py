"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeClusterVersionsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.integer_optional
    import aws_sdk_redshift.types.string


class DescribeClusterVersionsMessage(TypedDict):
    cluster_version: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The specific cluster version to return.</p> <p>Example: <code>1.0</code> </p>"""
    cluster_parameter_group_family: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The name of a specific cluster parameter group family to return details for.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 alphanumeric characters</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens</p> </li> </ul>"""
    max_records: NotRequired["aws_sdk_redshift.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>"""
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeClusterVersions</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeClusterVersionsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_version" in value:
        pairs.append((f"{prefix}.ClusterVersion", str(value["cluster_version"])))
    if "cluster_parameter_group_family" in value:
        pairs.append(
            (
                f"{prefix}.ClusterParameterGroupFamily",
                str(value["cluster_parameter_group_family"]),
            )
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeClusterVersionsMessage:
    out: DescribeClusterVersionsMessage = {}  # type: ignore[typeddict-item]
    child_cluster_version = el.find("ClusterVersion")
    if child_cluster_version is not None:
        out["cluster_version"] = str(child_cluster_version.text or "")
    child_cluster_parameter_group_family = el.find("ClusterParameterGroupFamily")
    if child_cluster_parameter_group_family is not None:
        out["cluster_parameter_group_family"] = str(
            child_cluster_parameter_group_family.text or ""
        )
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
