"""Generated from Smithy shape ``com.amazonaws.redshift#OrderableClusterOptionsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.orderable_cluster_options_list
    import capo_redshift.types.string


class OrderableClusterOptionsMessage(TypedDict, closed=True):
    orderable_cluster_options: NotRequired[
        "capo_redshift.types.orderable_cluster_options_list.OrderableClusterOptionsList"
    ]
    """<p>An <code>OrderableClusterOption</code> structure containing information about orderable options for the cluster.</p>"""
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the <code>Marker</code> parameter and retrying the command. If the <code>Marker</code> field is empty, all response records have been retrieved for the request. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OrderableClusterOptionsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "orderable_cluster_options" in value:
        import capo_redshift.types.orderable_cluster_options_list

        capo_redshift.types.orderable_cluster_options_list.serialize_query(
            value["orderable_cluster_options"],
            pairs,
            f"{prefix}.OrderableClusterOptions",
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> OrderableClusterOptionsMessage:
    out: OrderableClusterOptionsMessage = {}  # type: ignore[typeddict-item]
    child_orderable_cluster_options = el.find("OrderableClusterOptions")
    if child_orderable_cluster_options is not None:
        import capo_redshift.types.orderable_cluster_options_list

        out["orderable_cluster_options"] = (
            capo_redshift.types.orderable_cluster_options_list.deserialize_query(
                child_orderable_cluster_options
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
