"""Generated from Smithy shape ``com.amazonaws.neptune#SwitchoverGlobalClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.global_cluster_identifier
    import capo_neptune.types.string


class SwitchoverGlobalClusterMessage(TypedDict, closed=True):
    global_cluster_identifier: NotRequired[
        "capo_neptune.types.global_cluster_identifier.GlobalClusterIdentifier"
    ]
    """<p>The identifier of the global database cluster to switch over. This parameter isn't case-sensitive.</p> <p>Constraints: Must match the identifier of an existing global database cluster.</p>"""
    target_db_cluster_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the secondary Neptune DB cluster that you want to promote to primary for the global database.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SwitchoverGlobalClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "global_cluster_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}GlobalClusterIdentifier",
                str(value["global_cluster_identifier"]),
            )
        )
    if "target_db_cluster_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}TargetDbClusterIdentifier",
                str(value["target_db_cluster_identifier"]),
            )
        )


def deserialize_query(el: Element) -> SwitchoverGlobalClusterMessage:
    out: SwitchoverGlobalClusterMessage = {}  # type: ignore[typeddict-item]
    child_global_cluster_identifier = el.find("GlobalClusterIdentifier")
    if child_global_cluster_identifier is not None:
        out["global_cluster_identifier"] = str(
            child_global_cluster_identifier.text or ""
        )
    child_target_db_cluster_identifier = el.find("TargetDbClusterIdentifier")
    if child_target_db_cluster_identifier is not None:
        out["target_db_cluster_identifier"] = str(
            child_target_db_cluster_identifier.text or ""
        )
    return out
