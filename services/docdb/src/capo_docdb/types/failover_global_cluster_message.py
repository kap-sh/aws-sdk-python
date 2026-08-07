"""Generated from Smithy shape ``com.amazonaws.docdb#FailoverGlobalClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.boolean_optional
    import capo_docdb.types.db_cluster_identifier
    import capo_docdb.types.global_cluster_identifier


class FailoverGlobalClusterMessage(TypedDict, closed=True):
    global_cluster_identifier: NotRequired[
        "capo_docdb.types.global_cluster_identifier.GlobalClusterIdentifier"
    ]
    """<p>The identifier of the Amazon DocumentDB global cluster to apply this operation. The identifier is the unique key assigned by the user when the cluster is created. In other words, it's the name of the global cluster.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing global cluster.</p> </li> <li> <p>Minimum length of 1. Maximum length of 255.</p> </li> </ul> <p>Pattern: <code>[A-Za-z][0-9A-Za-z-:._]*</code> </p>"""
    target_db_cluster_identifier: NotRequired[
        "capo_docdb.types.db_cluster_identifier.DBClusterIdentifier"
    ]
    """<p>The identifier of the secondary Amazon DocumentDB cluster that you want to promote to the primary for the global cluster. Use the Amazon Resource Name (ARN) for the identifier so that Amazon DocumentDB can locate the cluster in its Amazon Web Services region.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing secondary cluster.</p> </li> <li> <p>Minimum length of 1. Maximum length of 255.</p> </li> </ul> <p>Pattern: <code>[A-Za-z][0-9A-Za-z-:._]*</code> </p>"""
    allow_data_loss: NotRequired["capo_docdb.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to allow data loss for this global cluster operation. Allowing data loss triggers a global failover operation.</p> <p>If you don't specify <code>AllowDataLoss</code>, the global cluster operation defaults to a switchover.</p> <p>Constraints:</p> <ul> <li> <p>Can't be specified together with the <code>Switchover</code> parameter.</p> </li> </ul>"""
    switchover: NotRequired["capo_docdb.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to switch over this global database cluster.</p> <p>Constraints:</p> <ul> <li> <p>Can't be specified together with the <code>AllowDataLoss</code> parameter.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: FailoverGlobalClusterMessage, pairs: list[tuple[str, str]], prefix: str
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
    if "allow_data_loss" in value:
        pairs.append(
            (
                f"{key_prefix}AllowDataLoss",
                "true" if value["allow_data_loss"] else "false",
            )
        )
    if "switchover" in value:
        pairs.append(
            (f"{key_prefix}Switchover", "true" if value["switchover"] else "false")
        )


def deserialize_query(el: Element) -> FailoverGlobalClusterMessage:
    out: FailoverGlobalClusterMessage = {}  # type: ignore[typeddict-item]
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
    child_allow_data_loss = el.find("AllowDataLoss")
    if child_allow_data_loss is not None:
        out["allow_data_loss"] = (child_allow_data_loss.text or "").lower() == "true"
    child_switchover = el.find("Switchover")
    if child_switchover is not None:
        out["switchover"] = (child_switchover.text or "").lower() == "true"
    return out
