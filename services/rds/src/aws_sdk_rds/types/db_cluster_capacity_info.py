"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterCapacityInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.integer_optional
    import aws_sdk_rds.types.string


class DBClusterCapacityInfo(TypedDict):
    db_cluster_identifier: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>A user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.</p>"""
    pending_capacity: NotRequired["aws_sdk_rds.types.integer_optional.IntegerOptional"]
    """<p>A value that specifies the capacity that the DB cluster scales to next.</p>"""
    current_capacity: NotRequired["aws_sdk_rds.types.integer_optional.IntegerOptional"]
    """<p>The current capacity of the DB cluster.</p>"""
    seconds_before_timeout: NotRequired[
        "aws_sdk_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of seconds before a call to <code>ModifyCurrentDBClusterCapacity</code> times out.</p>"""
    timeout_action: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The timeout action of a call to <code>ModifyCurrentDBClusterCapacity</code>, either <code>ForceApplyCapacityChange</code> or <code>RollbackCapacityChange</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterCapacityInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{prefix}.DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "pending_capacity" in value:
        pairs.append((f"{prefix}.PendingCapacity", str(value["pending_capacity"])))
    if "current_capacity" in value:
        pairs.append((f"{prefix}.CurrentCapacity", str(value["current_capacity"])))
    if "seconds_before_timeout" in value:
        pairs.append(
            (f"{prefix}.SecondsBeforeTimeout", str(value["seconds_before_timeout"]))
        )
    if "timeout_action" in value:
        pairs.append((f"{prefix}.TimeoutAction", str(value["timeout_action"])))


def deserialize_query(el: Element) -> DBClusterCapacityInfo:
    out: DBClusterCapacityInfo = {}  # type: ignore[typeddict-item]
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_pending_capacity = el.find("PendingCapacity")
    if child_pending_capacity is not None:
        out["pending_capacity"] = int(child_pending_capacity.text or "")
    child_current_capacity = el.find("CurrentCapacity")
    if child_current_capacity is not None:
        out["current_capacity"] = int(child_current_capacity.text or "")
    child_seconds_before_timeout = el.find("SecondsBeforeTimeout")
    if child_seconds_before_timeout is not None:
        out["seconds_before_timeout"] = int(child_seconds_before_timeout.text or "")
    child_timeout_action = el.find("TimeoutAction")
    if child_timeout_action is not None:
        out["timeout_action"] = str(child_timeout_action.text or "")
    return out
