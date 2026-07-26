"""Generated from Smithy shape ``com.amazonaws.neptune#FailoverGlobalClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.boolean_optional
    import capo_neptune.types.global_cluster_identifier
    import capo_neptune.types.string


class FailoverGlobalClusterMessage(TypedDict, closed=True):
    global_cluster_identifier: NotRequired[
        "capo_neptune.types.global_cluster_identifier.GlobalClusterIdentifier"
    ]
    """<p>Identifier of the Neptune global database that should be failed over. The identifier is the unique key assigned by the user when the Neptune global database was created. In other words, it's the name of the global database that you want to fail over.</p> <p>Constraints: Must match the identifier of an existing Neptune global database.</p>"""
    target_db_cluster_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the secondary Neptune DB cluster that you want to promote to primary for the global database.</p>"""
    allow_data_loss: NotRequired["capo_neptune.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to allow data loss for this global database cluster operation. Allowing data loss triggers a global failover operation.</p> <p>If you don't specify <code>AllowDataLoss</code>, the global database cluster operation defaults to a switchover.</p> <p>Constraints: Can't be specified together with the <code>Switchover</code> parameter.</p>"""
    switchover: NotRequired["capo_neptune.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to switch over this global database cluster.</p> <p>Constraints: Can't be specified together with the <code>AllowDataLoss</code> parameter.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: FailoverGlobalClusterMessage, pairs: list[tuple[str, str]], prefix: str
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
    if "allow_data_loss" in value:
        pairs.append(
            (f"{prefix}.AllowDataLoss", "true" if value["allow_data_loss"] else "false")
        )
    if "switchover" in value:
        pairs.append(
            (f"{prefix}.Switchover", "true" if value["switchover"] else "false")
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
