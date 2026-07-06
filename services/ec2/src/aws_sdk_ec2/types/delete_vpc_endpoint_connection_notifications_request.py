"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteVpcEndpointConnectionNotificationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.connection_notification_ids_list


class DeleteVpcEndpointConnectionNotificationsRequest(TypedDict, closed=True):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    connection_notification_ids: NotRequired[
        "aws_sdk_ec2.types.connection_notification_ids_list.ConnectionNotificationIdsList"
    ]
    """<p>The IDs of the notifications.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteVpcEndpointConnectionNotificationsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "connection_notification_ids" in value:
        import aws_sdk_ec2.types.connection_notification_ids_list

        aws_sdk_ec2.types.connection_notification_ids_list.serialize_ec2_query(
            value["connection_notification_ids"],
            pairs,
            f"{prefix}.ConnectionNotificationIds",
        )


def deserialize_ec2_query(
    el: Element,
) -> DeleteVpcEndpointConnectionNotificationsRequest:
    out: DeleteVpcEndpointConnectionNotificationsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("ConnectionNotificationIds") is not None:
        import aws_sdk_ec2.types.connection_notification_ids_list

        out["connection_notification_ids"] = (
            aws_sdk_ec2.types.connection_notification_ids_list.deserialize_ec2_query(
                el, "ConnectionNotificationIds"
            )
        )
    return out
