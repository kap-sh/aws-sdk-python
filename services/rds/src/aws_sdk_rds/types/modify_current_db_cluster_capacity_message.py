"""Generated from Smithy shape ``com.amazonaws.rds#ModifyCurrentDBClusterCapacityMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.integer_optional
    import aws_sdk_rds.types.string


class ModifyCurrentDBClusterCapacityMessage(TypedDict, closed=True):
    db_cluster_identifier: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The DB cluster identifier for the cluster being modified. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing DB cluster.</p> </li> </ul>"""
    capacity: NotRequired["aws_sdk_rds.types.integer_optional.IntegerOptional"]
    """<p>The DB cluster capacity.</p> <p>When you change the capacity of a paused Aurora Serverless v1 DB cluster, it automatically resumes.</p> <p>Constraints:</p> <ul> <li> <p>For Aurora MySQL, valid capacity values are <code>1</code>, <code>2</code>, <code>4</code>, <code>8</code>, <code>16</code>, <code>32</code>, <code>64</code>, <code>128</code>, and <code>256</code>.</p> </li> <li> <p>For Aurora PostgreSQL, valid capacity values are <code>2</code>, <code>4</code>, <code>8</code>, <code>16</code>, <code>32</code>, <code>64</code>, <code>192</code>, and <code>384</code>.</p> </li> </ul>"""
    seconds_before_timeout: NotRequired[
        "aws_sdk_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The amount of time, in seconds, that Aurora Serverless v1 tries to find a scaling point to perform seamless scaling before enforcing the timeout action. The default is 300.</p> <p>Specify a value between 10 and 600 seconds.</p>"""
    timeout_action: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The action to take when the timeout is reached, either <code>ForceApplyCapacityChange</code> or <code>RollbackCapacityChange</code>.</p> <p> <code>ForceApplyCapacityChange</code>, the default, sets the capacity to the specified value as soon as possible.</p> <p> <code>RollbackCapacityChange</code> ignores the capacity change if a scaling point isn't found in the timeout period.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyCurrentDBClusterCapacityMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{prefix}.DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "capacity" in value:
        pairs.append((f"{prefix}.Capacity", str(value["capacity"])))
    if "seconds_before_timeout" in value:
        pairs.append(
            (f"{prefix}.SecondsBeforeTimeout", str(value["seconds_before_timeout"]))
        )
    if "timeout_action" in value:
        pairs.append((f"{prefix}.TimeoutAction", str(value["timeout_action"])))


def deserialize_query(el: Element) -> ModifyCurrentDBClusterCapacityMessage:
    out: ModifyCurrentDBClusterCapacityMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_capacity = el.find("Capacity")
    if child_capacity is not None:
        out["capacity"] = int(child_capacity.text or "")
    child_seconds_before_timeout = el.find("SecondsBeforeTimeout")
    if child_seconds_before_timeout is not None:
        out["seconds_before_timeout"] = int(child_seconds_before_timeout.text or "")
    child_timeout_action = el.find("TimeoutAction")
    if child_timeout_action is not None:
        out["timeout_action"] = str(child_timeout_action.text or "")
    return out
