"""Generated from Smithy shape ``com.amazonaws.ec2#ConnectionNotification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.connection_notification_state
    import capo_ec2.types.connection_notification_type
    import capo_ec2.types.string
    import capo_ec2.types.value_string_list


class ConnectionNotification(TypedDict, closed=True):
    connection_notification_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the notification.</p>"""
    service_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the endpoint service.</p>"""
    vpc_endpoint_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC endpoint.</p>"""
    connection_notification_type: NotRequired[
        "capo_ec2.types.connection_notification_type.ConnectionNotificationType"
    ]
    """<p>The type of notification.</p>"""
    connection_notification_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The ARN of the SNS topic for the notification.</p>"""
    connection_events: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The events for the notification. Valid values are <code>Accept</code>, <code>Connect</code>, <code>Delete</code>, and <code>Reject</code>.</p>"""
    connection_notification_state: NotRequired[
        "capo_ec2.types.connection_notification_state.ConnectionNotificationState"
    ]
    """<p>The state of the notification.</p>"""
    service_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Region for the endpoint service.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ConnectionNotification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "connection_notification_id" in value:
        pairs.append(
            (
                f"{key_prefix}ConnectionNotificationId",
                str(value["connection_notification_id"]),
            )
        )
    if "service_id" in value:
        pairs.append((f"{key_prefix}ServiceId", str(value["service_id"])))
    if "vpc_endpoint_id" in value:
        pairs.append((f"{key_prefix}VpcEndpointId", str(value["vpc_endpoint_id"])))
    if "connection_notification_type" in value:
        import capo_ec2.types.connection_notification_type

        capo_ec2.types.connection_notification_type.serialize_ec2_query(
            value["connection_notification_type"],
            pairs,
            f"{key_prefix}ConnectionNotificationType",
        )
    if "connection_notification_arn" in value:
        pairs.append(
            (
                f"{key_prefix}ConnectionNotificationArn",
                str(value["connection_notification_arn"]),
            )
        )
    if "connection_events" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["connection_events"], pairs, f"{key_prefix}ConnectionEvents"
        )
    if "connection_notification_state" in value:
        import capo_ec2.types.connection_notification_state

        capo_ec2.types.connection_notification_state.serialize_ec2_query(
            value["connection_notification_state"],
            pairs,
            f"{key_prefix}ConnectionNotificationState",
        )
    if "service_region" in value:
        pairs.append((f"{key_prefix}ServiceRegion", str(value["service_region"])))


def deserialize_ec2_query(el: Element) -> ConnectionNotification:
    out: ConnectionNotification = {}  # type: ignore[typeddict-item]
    child_connection_notification_id = el.find("ConnectionNotificationId")
    if child_connection_notification_id is not None:
        out["connection_notification_id"] = str(
            child_connection_notification_id.text or ""
        )
    child_service_id = el.find("ServiceId")
    if child_service_id is not None:
        out["service_id"] = str(child_service_id.text or "")
    child_vpc_endpoint_id = el.find("VpcEndpointId")
    if child_vpc_endpoint_id is not None:
        out["vpc_endpoint_id"] = str(child_vpc_endpoint_id.text or "")
    child_connection_notification_type = el.find("ConnectionNotificationType")
    if child_connection_notification_type is not None:
        import capo_ec2.types.connection_notification_type

        out["connection_notification_type"] = (
            capo_ec2.types.connection_notification_type.deserialize_ec2_query(
                child_connection_notification_type
            )
        )
    child_connection_notification_arn = el.find("ConnectionNotificationArn")
    if child_connection_notification_arn is not None:
        out["connection_notification_arn"] = str(
            child_connection_notification_arn.text or ""
        )
    if el.find("ConnectionEvents") is not None:
        import capo_ec2.types.value_string_list

        out["connection_events"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                el, "ConnectionEvents"
            )
        )
    child_connection_notification_state = el.find("ConnectionNotificationState")
    if child_connection_notification_state is not None:
        import capo_ec2.types.connection_notification_state

        out["connection_notification_state"] = (
            capo_ec2.types.connection_notification_state.deserialize_ec2_query(
                child_connection_notification_state
            )
        )
    child_service_region = el.find("ServiceRegion")
    if child_service_region is not None:
        out["service_region"] = str(child_service_region.text or "")
    return out
