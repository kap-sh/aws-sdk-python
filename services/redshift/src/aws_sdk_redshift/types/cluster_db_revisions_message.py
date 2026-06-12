"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterDbRevisionsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.cluster_db_revisions_list
    import aws_sdk_redshift.types.string


class ClusterDbRevisionsMessage(TypedDict):
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A string representing the starting point for the next set of revisions. If a value is returned in a response, you can retrieve the next set of revisions by providing the value in the <code>marker</code> parameter and retrying the command. If the <code>marker</code> field is empty, all revisions have already been returned.</p>"""
    cluster_db_revisions: NotRequired[
        "aws_sdk_redshift.types.cluster_db_revisions_list.ClusterDbRevisionsList"
    ]
    """<p>A list of revisions.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterDbRevisionsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "cluster_db_revisions" in value:
        import aws_sdk_redshift.types.cluster_db_revisions_list

        aws_sdk_redshift.types.cluster_db_revisions_list.serialize_query(
            value["cluster_db_revisions"], pairs, f"{prefix}.ClusterDbRevisions"
        )


def deserialize_query(el: Element) -> ClusterDbRevisionsMessage:
    out: ClusterDbRevisionsMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_cluster_db_revisions = el.find("ClusterDbRevisions")
    if child_cluster_db_revisions is not None:
        import aws_sdk_redshift.types.cluster_db_revisions_list

        out["cluster_db_revisions"] = (
            aws_sdk_redshift.types.cluster_db_revisions_list.deserialize_query(
                child_cluster_db_revisions
            )
        )
    return out
