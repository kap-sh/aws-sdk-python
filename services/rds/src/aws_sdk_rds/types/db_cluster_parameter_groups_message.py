"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterParameterGroupsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_cluster_parameter_group_list
    import aws_sdk_rds.types.string


class DBClusterParameterGroupsMessage(TypedDict):
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeDBClusterParameterGroups</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    db_cluster_parameter_groups: NotRequired[
        "aws_sdk_rds.types.db_cluster_parameter_group_list.DBClusterParameterGroupList"
    ]
    """<p>A list of DB cluster parameter groups.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterParameterGroupsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "db_cluster_parameter_groups" in value:
        import aws_sdk_rds.types.db_cluster_parameter_group_list

        aws_sdk_rds.types.db_cluster_parameter_group_list.serialize_query(
            value["db_cluster_parameter_groups"],
            pairs,
            f"{prefix}.DBClusterParameterGroups",
        )


def deserialize_query(el: Element) -> DBClusterParameterGroupsMessage:
    out: DBClusterParameterGroupsMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_db_cluster_parameter_groups = el.find("DBClusterParameterGroups")
    if child_db_cluster_parameter_groups is not None:
        import aws_sdk_rds.types.db_cluster_parameter_group_list

        out["db_cluster_parameter_groups"] = (
            aws_sdk_rds.types.db_cluster_parameter_group_list.deserialize_query(
                child_db_cluster_parameter_groups
            )
        )
    return out
