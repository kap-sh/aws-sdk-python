"""Generated from Smithy shape ``com.amazonaws.rds#SwitchoverGlobalClusterMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_cluster_identifier
    import aws_sdk_rds.types.global_cluster_identifier


class SwitchoverGlobalClusterMessage(TypedDict):
    global_cluster_identifier: NotRequired[
        "aws_sdk_rds.types.global_cluster_identifier.GlobalClusterIdentifier"
    ]
    """<p>The identifier of the global database cluster to switch over. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing global database cluster (Aurora global database).</p> </li> </ul>"""
    target_db_cluster_identifier: NotRequired[
        "aws_sdk_rds.types.db_cluster_identifier.DBClusterIdentifier"
    ]
    """<p>The identifier of the secondary Aurora DB cluster to promote to the new primary for the global database cluster. Use the Amazon Resource Name (ARN) for the identifier so that Aurora can locate the cluster in its Amazon Web Services Region.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SwitchoverGlobalClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "global_cluster_identifier" in value:
        pairs.append(
            (
                f"{prefix}.GlobalClusterIdentifier",
                str(value["global_cluster_identifier"]),
            )
        )
    if "target_db_cluster_identifier" in value:
        pairs.append(
            (
                f"{prefix}.TargetDbClusterIdentifier",
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
