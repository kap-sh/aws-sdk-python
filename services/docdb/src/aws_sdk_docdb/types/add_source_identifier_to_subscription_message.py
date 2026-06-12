"""Generated from Smithy shape ``com.amazonaws.docdb#AddSourceIdentifierToSubscriptionMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.string


class AddSourceIdentifierToSubscriptionMessage(TypedDict):
    subscription_name: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The name of the Amazon DocumentDB event notification subscription that you want to add a source identifier to.</p>"""
    source_identifier: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The identifier of the event source to be added:</p> <ul> <li> <p>If the source type is an instance, a <code>DBInstanceIdentifier</code> must be provided.</p> </li> <li> <p>If the source type is a security group, a <code>DBSecurityGroupName</code> must be provided.</p> </li> <li> <p>If the source type is a parameter group, a <code>DBParameterGroupName</code> must be provided.</p> </li> <li> <p>If the source type is a snapshot, a <code>DBSnapshotIdentifier</code> must be provided.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AddSourceIdentifierToSubscriptionMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "subscription_name" in value:
        pairs.append((f"{prefix}.SubscriptionName", str(value["subscription_name"])))
    if "source_identifier" in value:
        pairs.append((f"{prefix}.SourceIdentifier", str(value["source_identifier"])))


def deserialize_query(el: Element) -> AddSourceIdentifierToSubscriptionMessage:
    out: AddSourceIdentifierToSubscriptionMessage = {}  # type: ignore[typeddict-item]
    child_subscription_name = el.find("SubscriptionName")
    if child_subscription_name is not None:
        out["subscription_name"] = str(child_subscription_name.text or "")
    child_source_identifier = el.find("SourceIdentifier")
    if child_source_identifier is not None:
        out["source_identifier"] = str(child_source_identifier.text or "")
    return out
