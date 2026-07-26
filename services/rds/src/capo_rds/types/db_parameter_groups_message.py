"""Generated from Smithy shape ``com.amazonaws.rds#DBParameterGroupsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_parameter_group_list
    import capo_rds.types.string


class DBParameterGroupsMessage(TypedDict, closed=True):
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    db_parameter_groups: NotRequired[
        "capo_rds.types.db_parameter_group_list.DBParameterGroupList"
    ]
    """<p>A list of <code>DBParameterGroup</code> instances.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBParameterGroupsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "db_parameter_groups" in value:
        import capo_rds.types.db_parameter_group_list

        capo_rds.types.db_parameter_group_list.serialize_query(
            value["db_parameter_groups"], pairs, f"{prefix}.DBParameterGroups"
        )


def deserialize_query(el: Element) -> DBParameterGroupsMessage:
    out: DBParameterGroupsMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_db_parameter_groups = el.find("DBParameterGroups")
    if child_db_parameter_groups is not None:
        import capo_rds.types.db_parameter_group_list

        out["db_parameter_groups"] = (
            capo_rds.types.db_parameter_group_list.deserialize_query(
                child_db_parameter_groups
            )
        )
    return out
