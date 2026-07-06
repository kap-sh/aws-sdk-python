"""Generated from Smithy shape ``com.amazonaws.notifications#GetNotificationConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.aggregation_duration
    import aws_sdk_notifications.types.creation_time
    import aws_sdk_notifications.types.notification_configuration_arn
    import aws_sdk_notifications.types.notification_configuration_description
    import aws_sdk_notifications.types.notification_configuration_name
    import aws_sdk_notifications.types.notification_configuration_status
    import aws_sdk_notifications.types.notification_configuration_subtype


class GetNotificationConfigurationResponse(TypedDict, closed=True):
    arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    """<p>The ARN of the resource.</p>"""
    name: "aws_sdk_notifications.types.notification_configuration_name.NotificationConfigurationName"
    """<p>The name of the <code>NotificationConfiguration</code>.</p>"""
    description: "aws_sdk_notifications.types.notification_configuration_description.NotificationConfigurationDescription"
    """<p>The description of the <code>NotificationConfiguration</code>.</p>"""
    status: "aws_sdk_notifications.types.notification_configuration_status.NotificationConfigurationStatus"
    """<p>The status of this <code>NotificationConfiguration</code>.</p>"""
    creation_time: "aws_sdk_notifications.types.creation_time.CreationTime"
    """<p>The creation time of the <code>NotificationConfiguration</code>.</p>"""
    aggregation_duration: NotRequired[
        "aws_sdk_notifications.types.aggregation_duration.AggregationDuration"
    ]
    """<p>The aggregation preference of the <code>NotificationConfiguration</code>.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>LONG</code> </p> <ul> <li> <p>Aggregate notifications for long periods of time (12 hours).</p> </li> </ul> </li> <li> <p> <code>SHORT</code> </p> <ul> <li> <p>Aggregate notifications for short periods of time (5 minutes).</p> </li> </ul> </li> <li> <p> <code>NONE</code> </p> <ul> <li> <p>Don't aggregate notifications.</p> </li> </ul> </li> </ul> </li> </ul>"""
    subtype: NotRequired[
        "aws_sdk_notifications.types.notification_configuration_subtype.NotificationConfigurationSubtype"
    ]
    """<p>The subtype of the notification configuration returned in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNotificationConfigurationResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["description"] = value["description"]
    out["status"] = value["status"]
    import aws_sdk_notifications.types.creation_time

    out["creationTime"] = aws_sdk_notifications.types.creation_time.serialize_json(
        value["creation_time"]
    )
    if "aggregation_duration" in value:
        out["aggregationDuration"] = value["aggregation_duration"]
    if "subtype" in value:
        out["subtype"] = value["subtype"]
    return out


def deserialize_json(data: dict) -> GetNotificationConfigurationResponse:
    out: GetNotificationConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetNotificationConfigurationResponse.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetNotificationConfigurationResponse.name required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError(
            "GetNotificationConfigurationResponse.description required"
        )
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError(
            "GetNotificationConfigurationResponse.status required"
        )
    if "creationTime" in data:
        import aws_sdk_notifications.types.creation_time

        out["creation_time"] = (
            aws_sdk_notifications.types.creation_time.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetNotificationConfigurationResponse.creation_time required"
        )
    if "aggregationDuration" in data:
        out["aggregation_duration"] = data["aggregationDuration"]
    if "subtype" in data:
        out["subtype"] = data["subtype"]
    return out
