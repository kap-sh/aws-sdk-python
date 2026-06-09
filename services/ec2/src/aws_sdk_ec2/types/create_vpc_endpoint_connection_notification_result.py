"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpcEndpointConnectionNotificationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.connection_notification
    import aws_sdk_ec2.types.string


class CreateVpcEndpointConnectionNotificationResult(TypedDict):
    connection_notification: NotRequired[
        "aws_sdk_ec2.types.connection_notification.ConnectionNotification"
    ]
    """<p>Information about the notification.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVpcEndpointConnectionNotificationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "connection_notification" in value:
        import aws_sdk_ec2.types.connection_notification

        aws_sdk_ec2.types.connection_notification.serialize_ec2_query(
            value["connection_notification"], pairs, f"{prefix}.ConnectionNotification"
        )
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> CreateVpcEndpointConnectionNotificationResult:
    out: CreateVpcEndpointConnectionNotificationResult = {}  # type: ignore[typeddict-item]
    child_connection_notification = el.find("ConnectionNotification")
    if child_connection_notification is not None:
        import aws_sdk_ec2.types.connection_notification

        out["connection_notification"] = (
            aws_sdk_ec2.types.connection_notification.deserialize_ec2_query(
                child_connection_notification
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
