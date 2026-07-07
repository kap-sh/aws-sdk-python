"""Generated from Smithy shape ``com.amazonaws.neptune#RemoveFromGlobalClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.global_cluster_identifier
    import aws_sdk_neptune.types.string


class RemoveFromGlobalClusterMessage(TypedDict, closed=True):
    global_cluster_identifier: NotRequired[
        "aws_sdk_neptune.types.global_cluster_identifier.GlobalClusterIdentifier"
    ]
    """<p>The identifier of the Neptune global database from which to detach the specified Neptune DB cluster.</p>"""
    db_cluster_identifier: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The Amazon Resource Name (ARN) identifying the cluster to be detached from the Neptune global database cluster.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RemoveFromGlobalClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "global_cluster_identifier" in value:
        pairs.append(
            (
                f"{prefix}.GlobalClusterIdentifier",
                str(value["global_cluster_identifier"]),
            )
        )
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{prefix}.DbClusterIdentifier", str(value["db_cluster_identifier"]))
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
