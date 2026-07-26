"""Generated from Smithy shape ``com.amazonaws.rds#DescribeBlueGreenDeploymentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.blue_green_deployment_identifier
    import capo_rds.types.filter_list
    import capo_rds.types.max_records
    import capo_rds.types.string


class DescribeBlueGreenDeploymentsRequest(TypedDict, closed=True):
    blue_green_deployment_identifier: NotRequired[
        "capo_rds.types.blue_green_deployment_identifier.BlueGreenDeploymentIdentifier"
    ]
    """<p>The blue/green deployment identifier. If you specify this parameter, the response only includes information about the specific blue/green deployment. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match an existing blue/green deployment identifier.</p> </li> </ul>"""
    filters: NotRequired["capo_rds.types.filter_list.FilterList"]
    """<p>A filter that specifies one or more blue/green deployments to describe.</p> <p>Valid Values:</p> <ul> <li> <p> <code>blue-green-deployment-identifier</code> - Accepts system-generated identifiers for blue/green deployments. The results list only includes information about the blue/green deployments with the specified identifiers.</p> </li> <li> <p> <code>blue-green-deployment-name</code> - Accepts user-supplied names for blue/green deployments. The results list only includes information about the blue/green deployments with the specified names.</p> </li> <li> <p> <code>source</code> - Accepts source databases for a blue/green deployment. The results list only includes information about the blue/green deployments with the specified source databases.</p> </li> <li> <p> <code>target</code> - Accepts target databases for a blue/green deployment. The results list only includes information about the blue/green deployments with the specified target databases.</p> </li> </ul>"""
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeBlueGreenDeployments</code> request. If you specify this parameter, the response only includes records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    max_records: NotRequired["capo_rds.types.max_records.MaxRecords"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so you can retrieve the remaining results.</p> <p>Default: 100</p> <p>Constraints:</p> <ul> <li> <p>Must be a minimum of 20.</p> </li> <li> <p>Can't exceed 100.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeBlueGreenDeploymentsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "blue_green_deployment_identifier" in value:
        pairs.append(
            (
                f"{prefix}.BlueGreenDeploymentIdentifier",
                str(value["blue_green_deployment_identifier"]),
            )
        )
    if "filters" in value:
        import capo_rds.types.filter_list

        capo_rds.types.filter_list.serialize_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))


def deserialize_query(el: Element) -> DescribeBlueGreenDeploymentsRequest:
    out: DescribeBlueGreenDeploymentsRequest = {}  # type: ignore[typeddict-item]
    child_blue_green_deployment_identifier = el.find("BlueGreenDeploymentIdentifier")
    if child_blue_green_deployment_identifier is not None:
        out["blue_green_deployment_identifier"] = str(
            child_blue_green_deployment_identifier.text or ""
        )
    child_filters = el.find("Filters")
    if child_filters is not None:
        import capo_rds.types.filter_list

        out["filters"] = capo_rds.types.filter_list.deserialize_query(child_filters)
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    return out
