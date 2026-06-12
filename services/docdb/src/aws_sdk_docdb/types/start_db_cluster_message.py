"""Generated from Smithy shape ``com.amazonaws.docdb#StartDBClusterMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.string


class StartDBClusterMessage(TypedDict):
    db_cluster_identifier: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The identifier of the cluster to restart. Example: <code>docdb-2019-05-28-15-24-52</code> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StartDBClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{prefix}.DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )


def deserialize_query(el: Element) -> StartDBClusterMessage:
    out: StartDBClusterMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    return out
