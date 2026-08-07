"""Generated from Smithy shape ``com.amazonaws.neptune#DBClusterParameterGroupsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.db_cluster_parameter_group_list
    import capo_neptune.types.string


class DBClusterParameterGroupsMessage(TypedDict, closed=True):
    marker: NotRequired["capo_neptune.types.string.String"]
    """<p> An optional pagination token provided by a previous <code>DescribeDBClusterParameterGroups</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    db_cluster_parameter_groups: NotRequired[
        "capo_neptune.types.db_cluster_parameter_group_list.DBClusterParameterGroupList"
    ]
    """<p>A list of DB cluster parameter groups.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterParameterGroupsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "db_cluster_parameter_groups" in value:
        import capo_neptune.types.db_cluster_parameter_group_list

        capo_neptune.types.db_cluster_parameter_group_list.serialize_query(
            value["db_cluster_parameter_groups"],
            pairs,
            f"{key_prefix}DBClusterParameterGroups",
        )


def deserialize_query(el: Element) -> DBClusterParameterGroupsMessage:
    out: DBClusterParameterGroupsMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_db_cluster_parameter_groups = el.find("DBClusterParameterGroups")
    if child_db_cluster_parameter_groups is not None:
        import capo_neptune.types.db_cluster_parameter_group_list

        out["db_cluster_parameter_groups"] = (
            capo_neptune.types.db_cluster_parameter_group_list.deserialize_query(
                child_db_cluster_parameter_groups
            )
        )
    return out
