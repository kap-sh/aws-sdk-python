"""Generated from Smithy shape ``com.amazonaws.docdb#SwitchoverGlobalClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.db_cluster_identifier
    import aws_sdk_docdb.types.global_cluster_identifier


class SwitchoverGlobalClusterMessage(TypedDict, closed=True):
    global_cluster_identifier: NotRequired[
        "aws_sdk_docdb.types.global_cluster_identifier.GlobalClusterIdentifier"
    ]
    """<p>The identifier of the Amazon DocumentDB global database cluster to switch over. The identifier is the unique key assigned by the user when the cluster is created. In other words, it's the name of the global cluster. This parameter isn’t case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing global cluster (Amazon DocumentDB global database).</p> </li> <li> <p>Minimum length of 1. Maximum length of 255.</p> </li> </ul> <p>Pattern: <code>[A-Za-z][0-9A-Za-z-:._]*</code> </p>"""
    target_db_cluster_identifier: NotRequired[
        "aws_sdk_docdb.types.db_cluster_identifier.DBClusterIdentifier"
    ]
    """<p>The identifier of the secondary Amazon DocumentDB cluster to promote to the new primary for the global database cluster. Use the Amazon Resource Name (ARN) for the identifier so that Amazon DocumentDB can locate the cluster in its Amazon Web Services region.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing secondary cluster.</p> </li> <li> <p>Minimum length of 1. Maximum length of 255.</p> </li> </ul> <p>Pattern: <code>[A-Za-z][0-9A-Za-z-:._]*</code> </p>"""


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
