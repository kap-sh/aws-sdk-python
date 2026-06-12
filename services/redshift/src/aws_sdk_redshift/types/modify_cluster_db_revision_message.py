"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyClusterDbRevisionMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string


class ModifyClusterDbRevisionMessage(TypedDict):
    cluster_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The unique identifier of a cluster whose database revision you want to modify. </p> <p>Example: <code>examplecluster</code> </p>"""
    revision_target: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The identifier of the database revision. You can retrieve this value from the response to the <a>DescribeClusterDbRevisions</a> request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyClusterDbRevisionMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))
    if "revision_target" in value:
        pairs.append((f"{prefix}.RevisionTarget", str(value["revision_target"])))


def deserialize_query(el: Element) -> ModifyClusterDbRevisionMessage:
    out: ModifyClusterDbRevisionMessage = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_revision_target = el.find("RevisionTarget")
    if child_revision_target is not None:
        out["revision_target"] = str(child_revision_target.text or "")
    return out
