"""Generated from Smithy shape ``com.amazonaws.neptune#StopDBClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.string


class StopDBClusterMessage(TypedDict, closed=True):
    db_cluster_identifier: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The DB cluster identifier of the Neptune DB cluster to be stopped. This parameter is stored as a lowercase string.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StopDBClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{prefix}.DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )


def deserialize_query(el: Element) -> StopDBClusterMessage:
    out: StopDBClusterMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    return out
