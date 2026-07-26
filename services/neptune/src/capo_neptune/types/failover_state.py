"""Generated from Smithy shape ``com.amazonaws.neptune#FailoverState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.boolean
    import capo_neptune.types.failover_status
    import capo_neptune.types.string


class FailoverState(TypedDict, closed=True):
    status: NotRequired["capo_neptune.types.failover_status.FailoverStatus"]
    """<p>The current status of the global cluster. Possible values are as follows:</p> <ul> <li> <p>pending  The service received a request to switch over or fail over the global cluster. The global cluster's primary DB cluster and the specified secondary DB cluster are being verified before the operation starts.</p> </li> <li> <p>failing-over  Neptune is promoting the chosen secondary Neptune DB cluster to become the new primary DB cluster to fail over the global cluster.</p> </li> <li> <p>cancelling  The request to switch over or fail over the global cluster was cancelled and the primary Neptune DB cluster and the selected secondary Neptune DB cluster are returning to their previous states.</p> </li> <li> <p>switching-over  This status covers the range of Neptune internal operations that take place during the switchover process, such as demoting the primary Neptune DB cluster, promoting the secondary Neptune DB cluster, and synchronizing replicas.</p> </li> </ul>"""
    from_db_cluster_arn: NotRequired["capo_neptune.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Neptune DB cluster that is currently being demoted, and which is associated with this state.</p>"""
    to_db_cluster_arn: NotRequired["capo_neptune.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Neptune DB cluster that is currently being promoted, and which is associated with this state.</p>"""
    is_data_loss_allowed: NotRequired["capo_neptune.types.boolean.Boolean"]
    """<p>Indicates whether the operation is a global switchover or a global failover. If data loss is allowed, then the operation is a global failover. Otherwise, it's a switchover.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: FailoverState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "status" in value:
        import capo_neptune.types.failover_status

        capo_neptune.types.failover_status.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "from_db_cluster_arn" in value:
        pairs.append((f"{prefix}.FromDbClusterArn", str(value["from_db_cluster_arn"])))
    if "to_db_cluster_arn" in value:
        pairs.append((f"{prefix}.ToDbClusterArn", str(value["to_db_cluster_arn"])))
    if "is_data_loss_allowed" in value:
        pairs.append(
            (
                f"{prefix}.IsDataLossAllowed",
                "true" if value["is_data_loss_allowed"] else "false",
            )
        )


def deserialize_query(el: Element) -> FailoverState:
    out: FailoverState = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import capo_neptune.types.failover_status

        out["status"] = capo_neptune.types.failover_status.deserialize_query(
            child_status
        )
    child_from_db_cluster_arn = el.find("FromDbClusterArn")
    if child_from_db_cluster_arn is not None:
        out["from_db_cluster_arn"] = str(child_from_db_cluster_arn.text or "")
    child_to_db_cluster_arn = el.find("ToDbClusterArn")
    if child_to_db_cluster_arn is not None:
        out["to_db_cluster_arn"] = str(child_to_db_cluster_arn.text or "")
    child_is_data_loss_allowed = el.find("IsDataLossAllowed")
    if child_is_data_loss_allowed is not None:
        out["is_data_loss_allowed"] = (
            child_is_data_loss_allowed.text or ""
        ).lower() == "true"
    return out
