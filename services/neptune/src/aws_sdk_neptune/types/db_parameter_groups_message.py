"""Generated from Smithy shape ``com.amazonaws.neptune#DBParameterGroupsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.db_parameter_group_list
    import aws_sdk_neptune.types.string


class DBParameterGroupsMessage(TypedDict):
    marker: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    db_parameter_groups: NotRequired[
        "aws_sdk_neptune.types.db_parameter_group_list.DBParameterGroupList"
    ]
    """<p>A list of <a>DBParameterGroup</a> instances.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBParameterGroupsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "db_parameter_groups" in value:
        import aws_sdk_neptune.types.db_parameter_group_list

        aws_sdk_neptune.types.db_parameter_group_list.serialize_query(
            value["db_parameter_groups"], pairs, f"{prefix}.DBParameterGroups"
        )


def deserialize_query(el: Element) -> DBParameterGroupsMessage:
    out: DBParameterGroupsMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_db_parameter_groups = el.find("DBParameterGroups")
    if child_db_parameter_groups is not None:
        import aws_sdk_neptune.types.db_parameter_group_list

        out["db_parameter_groups"] = (
            aws_sdk_neptune.types.db_parameter_group_list.deserialize_query(
                child_db_parameter_groups
            )
        )
    return out
