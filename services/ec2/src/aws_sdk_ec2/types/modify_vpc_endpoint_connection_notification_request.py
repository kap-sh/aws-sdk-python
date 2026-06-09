"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcEndpointConnectionNotificationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.connection_notification_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list


class ModifyVpcEndpointConnectionNotificationRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    connection_notification_id: NotRequired[
        "aws_sdk_ec2.types.connection_notification_id.ConnectionNotificationId"
    ]
    """<p>The ID of the notification.</p>"""
    connection_notification_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN for the SNS topic for the notification.</p>"""
    connection_events: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The events for the endpoint. Valid values are <code>Accept</code>, <code>Connect</code>, <code>Delete</code>, and <code>Reject</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVpcEndpointConnectionNotificationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "connection_notification_id" in value:
        pairs.append(
            (
                f"{prefix}.ConnectionNotificationId",
                str(value["connection_notification_id"]),
            )
        )
    if "connection_notification_arn" in value:
        pairs.append(
            (
                f"{prefix}.ConnectionNotificationArn",
                str(value["connection_notification_arn"]),
            )
        )
    if "connection_events" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["connection_events"], pairs, f"{prefix}.ConnectionEvents"
        )


def deserialize_ec2_query(
    el: Element,
) -> ModifyVpcEndpointConnectionNotificationRequest:
    out: ModifyVpcEndpointConnectionNotificationRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_connection_notification_id = el.find("ConnectionNotificationId")
    if child_connection_notification_id is not None:
        out["connection_notification_id"] = str(
            child_connection_notification_id.text or ""
        )
    child_connection_notification_arn = el.find("ConnectionNotificationArn")
    if child_connection_notification_arn is not None:
        out["connection_notification_arn"] = str(
            child_connection_notification_arn.text or ""
        )
    if el.find("ConnectionEvents") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["connection_events"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "ConnectionEvents"
            )
        )
    return out
