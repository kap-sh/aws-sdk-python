"""Generated from Smithy shape ``com.amazonaws.neptune#DescribeGlobalClustersMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.global_cluster_identifier
    import aws_sdk_neptune.types.integer_optional
    import aws_sdk_neptune.types.string


class DescribeGlobalClustersMessage(TypedDict, closed=True):
    global_cluster_identifier: NotRequired[
        "aws_sdk_neptune.types.global_cluster_identifier.GlobalClusterIdentifier"
    ]
    """<p>The user-supplied DB cluster identifier. If this parameter is specified, only information about the specified DB cluster is returned. This parameter is not case-sensitive.</p> <p>Constraints: If supplied, must match an existing DB cluster identifier.</p>"""
    max_records: NotRequired["aws_sdk_neptune.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination marker token is included in the response that you can use to retrieve the remaining results.</p> <p>Default: <code>100</code> </p> <p>Constraints: Minimum 20, maximum 100.</p>"""
    marker: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>(<i>Optional</i>) A pagination token returned by a previous call to <code>DescribeGlobalClusters</code>. If this parameter is specified, the response will only include records beyond the marker, up to the number specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeGlobalClustersMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "global_cluster_identifier" in value:
        pairs.append(
            (
                f"{prefix}.GlobalClusterIdentifier",
                str(value["global_cluster_identifier"]),
            )
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeGlobalClustersMessage:
    out: DescribeGlobalClustersMessage = {}  # type: ignore[typeddict-item]
    child_global_cluster_identifier = el.find("GlobalClusterIdentifier")
    if child_global_cluster_identifier is not None:
        out["global_cluster_identifier"] = str(
            child_global_cluster_identifier.text or ""
        )
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
