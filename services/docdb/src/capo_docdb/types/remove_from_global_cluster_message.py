"""Generated from Smithy shape ``com.amazonaws.docdb#RemoveFromGlobalClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.global_cluster_identifier
    import capo_docdb.types.string


class RemoveFromGlobalClusterMessage(TypedDict, closed=True):
    global_cluster_identifier: NotRequired[
        "capo_docdb.types.global_cluster_identifier.GlobalClusterIdentifier"
    ]
    """<p>The cluster identifier to detach from the Amazon DocumentDB global cluster. </p>"""
    db_cluster_identifier: NotRequired["capo_docdb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) identifying the cluster that was detached from the Amazon DocumentDB global cluster. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RemoveFromGlobalClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "global_cluster_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}GlobalClusterIdentifier",
                str(value["global_cluster_identifier"]),
            )
        )
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}DbClusterIdentifier", str(value["db_cluster_identifier"]))
        )


def deserialize_query(el: Element) -> RemoveFromGlobalClusterMessage:
    out: RemoveFromGlobalClusterMessage = {}  # type: ignore[typeddict-item]
    child_global_cluster_identifier = el.find("GlobalClusterIdentifier")
    if child_global_cluster_identifier is not None:
        out["global_cluster_identifier"] = str(
            child_global_cluster_identifier.text or ""
        )
    child_db_cluster_identifier = el.find("DbClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    return out
