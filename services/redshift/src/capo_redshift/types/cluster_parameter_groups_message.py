"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterParameterGroupsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.parameter_group_list
    import capo_redshift.types.string


class ClusterParameterGroupsMessage(TypedDict, closed=True):
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the <code>Marker</code> parameter and retrying the command. If the <code>Marker</code> field is empty, all response records have been retrieved for the request. </p>"""
    parameter_groups: NotRequired[
        "capo_redshift.types.parameter_group_list.ParameterGroupList"
    ]
    """<p>A list of <a>ClusterParameterGroup</a> instances. Each instance describes one cluster parameter group. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterParameterGroupsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "parameter_groups" in value:
        import capo_redshift.types.parameter_group_list

        capo_redshift.types.parameter_group_list.serialize_query(
            value["parameter_groups"], pairs, f"{prefix}.ParameterGroups"
        )


def deserialize_query(el: Element) -> ClusterParameterGroupsMessage:
    out: ClusterParameterGroupsMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_parameter_groups = el.find("ParameterGroups")
    if child_parameter_groups is not None:
        import capo_redshift.types.parameter_group_list

        out["parameter_groups"] = (
            capo_redshift.types.parameter_group_list.deserialize_query(
                child_parameter_groups
            )
        )
    return out
