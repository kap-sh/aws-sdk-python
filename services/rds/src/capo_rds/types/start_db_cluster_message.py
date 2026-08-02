"""Generated from Smithy shape ``com.amazonaws.rds#StartDBClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string


class StartDBClusterMessage(TypedDict, closed=True):
    db_cluster_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The DB cluster identifier of the Amazon Aurora DB cluster to be started. This parameter is stored as a lowercase string.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StartDBClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )


def deserialize_query(el: Element) -> StartDBClusterMessage:
    out: StartDBClusterMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    return out
