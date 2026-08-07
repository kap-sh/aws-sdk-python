"""Generated from Smithy shape ``com.amazonaws.redshift#ReservedNodesMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.reserved_node_list
    import capo_redshift.types.string


class ReservedNodesMessage(TypedDict, closed=True):
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the <code>Marker</code> parameter and retrying the command. If the <code>Marker</code> field is empty, all response records have been retrieved for the request. </p>"""
    reserved_nodes: NotRequired[
        "capo_redshift.types.reserved_node_list.ReservedNodeList"
    ]
    """<p>The list of <code>ReservedNode</code> objects.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReservedNodesMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "reserved_nodes" in value:
        import capo_redshift.types.reserved_node_list

        capo_redshift.types.reserved_node_list.serialize_query(
            value["reserved_nodes"], pairs, f"{key_prefix}ReservedNodes"
        )


def deserialize_query(el: Element) -> ReservedNodesMessage:
    out: ReservedNodesMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_reserved_nodes = el.find("ReservedNodes")
    if child_reserved_nodes is not None:
        import capo_redshift.types.reserved_node_list

        out["reserved_nodes"] = (
            capo_redshift.types.reserved_node_list.deserialize_query(
                child_reserved_nodes
            )
        )
    return out
