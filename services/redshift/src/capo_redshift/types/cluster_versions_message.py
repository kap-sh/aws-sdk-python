"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterVersionsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.cluster_version_list
    import capo_redshift.types.string


class ClusterVersionsMessage(TypedDict, closed=True):
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the <code>Marker</code> parameter and retrying the command. If the <code>Marker</code> field is empty, all response records have been retrieved for the request. </p>"""
    cluster_versions: NotRequired[
        "capo_redshift.types.cluster_version_list.ClusterVersionList"
    ]
    """<p>A list of <code>Version</code> elements. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterVersionsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "cluster_versions" in value:
        import capo_redshift.types.cluster_version_list

        capo_redshift.types.cluster_version_list.serialize_query(
            value["cluster_versions"], pairs, f"{prefix}.ClusterVersions"
        )


def deserialize_query(el: Element) -> ClusterVersionsMessage:
    out: ClusterVersionsMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_cluster_versions = el.find("ClusterVersions")
    if child_cluster_versions is not None:
        import capo_redshift.types.cluster_version_list

        out["cluster_versions"] = (
            capo_redshift.types.cluster_version_list.deserialize_query(
                child_cluster_versions
            )
        )
    return out
