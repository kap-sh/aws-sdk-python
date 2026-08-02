"""Generated from Smithy shape ``com.amazonaws.rds#AddSourceIdentifierToSubscriptionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string


class AddSourceIdentifierToSubscriptionMessage(TypedDict, closed=True):
    subscription_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the RDS event notification subscription you want to add a source identifier to.</p>"""
    source_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier of the event source to be added.</p> <p>Constraints:</p> <ul> <li> <p>If the source type is a DB instance, a <code>DBInstanceIdentifier</code> value must be supplied.</p> </li> <li> <p>If the source type is a DB cluster, a <code>DBClusterIdentifier</code> value must be supplied.</p> </li> <li> <p>If the source type is a DB parameter group, a <code>DBParameterGroupName</code> value must be supplied.</p> </li> <li> <p>If the source type is a DB security group, a <code>DBSecurityGroupName</code> value must be supplied.</p> </li> <li> <p>If the source type is a DB snapshot, a <code>DBSnapshotIdentifier</code> value must be supplied.</p> </li> <li> <p>If the source type is a DB cluster snapshot, a <code>DBClusterSnapshotIdentifier</code> value must be supplied.</p> </li> <li> <p>If the source type is an RDS Proxy, a <code>DBProxyName</code> value must be supplied.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AddSourceIdentifierToSubscriptionMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "subscription_name" in value:
        pairs.append((f"{key_prefix}SubscriptionName", str(value["subscription_name"])))
    if "source_identifier" in value:
        pairs.append((f"{key_prefix}SourceIdentifier", str(value["source_identifier"])))


def deserialize_query(el: Element) -> AddSourceIdentifierToSubscriptionMessage:
    out: AddSourceIdentifierToSubscriptionMessage = {}  # type: ignore[typeddict-item]
    child_subscription_name = el.find("SubscriptionName")
    if child_subscription_name is not None:
        out["subscription_name"] = str(child_subscription_name.text or "")
    child_source_identifier = el.find("SourceIdentifier")
    if child_source_identifier is not None:
        out["source_identifier"] = str(child_source_identifier.text or "")
    return out
