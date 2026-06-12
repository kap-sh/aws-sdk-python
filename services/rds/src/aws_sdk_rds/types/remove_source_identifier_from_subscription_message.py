"""Generated from Smithy shape ``com.amazonaws.rds#RemoveSourceIdentifierFromSubscriptionMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string


class RemoveSourceIdentifierFromSubscriptionMessage(TypedDict):
    subscription_name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the RDS event notification subscription you want to remove a source identifier from.</p>"""
    source_identifier: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The source identifier to be removed from the subscription, such as the <b>DB instance identifier</b> for a DB instance or the name of a security group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RemoveSourceIdentifierFromSubscriptionMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "subscription_name" in value:
        pairs.append((f"{prefix}.SubscriptionName", str(value["subscription_name"])))
    if "source_identifier" in value:
        pairs.append((f"{prefix}.SourceIdentifier", str(value["source_identifier"])))


def deserialize_query(el: Element) -> RemoveSourceIdentifierFromSubscriptionMessage:
    out: RemoveSourceIdentifierFromSubscriptionMessage = {}  # type: ignore[typeddict-item]
    child_subscription_name = el.find("SubscriptionName")
    if child_subscription_name is not None:
        out["subscription_name"] = str(child_subscription_name.text or "")
    child_source_identifier = el.find("SourceIdentifier")
    if child_source_identifier is not None:
        out["source_identifier"] = str(child_source_identifier.text or "")
    return out
