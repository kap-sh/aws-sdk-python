"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpcEndpointConnectionNotificationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.connection_notification
    import capo_ec2.types.string


class CreateVpcEndpointConnectionNotificationResult(TypedDict, closed=True):
    connection_notification: NotRequired[
        "capo_ec2.types.connection_notification.ConnectionNotification"
    ]
    """<p>Information about the notification.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVpcEndpointConnectionNotificationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "connection_notification" in value:
        import capo_ec2.types.connection_notification

        capo_ec2.types.connection_notification.serialize_ec2_query(
            value["connection_notification"],
            pairs,
            f"{key_prefix}ConnectionNotification",
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> CreateVpcEndpointConnectionNotificationResult:
    out: CreateVpcEndpointConnectionNotificationResult = {}  # type: ignore[typeddict-item]
    child_connection_notification = el.find("connectionNotification")
    if child_connection_notification is not None:
        import capo_ec2.types.connection_notification

        out["connection_notification"] = (
            capo_ec2.types.connection_notification.deserialize_ec2_query(
                child_connection_notification
            )
        )
    child_client_token = el.find("clientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
