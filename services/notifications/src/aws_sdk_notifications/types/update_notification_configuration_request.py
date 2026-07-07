"""Generated from Smithy shape ``com.amazonaws.notifications#UpdateNotificationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_notifications.types.aggregation_duration
    import aws_sdk_notifications.types.notification_configuration_arn
    import aws_sdk_notifications.types.notification_configuration_description
    import aws_sdk_notifications.types.notification_configuration_name


class UpdateNotificationConfigurationRequest(TypedDict, closed=True):
    arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    """<p>The Amazon Resource Name (ARN) used to update the <code>NotificationConfiguration</code>.</p>"""
    name: NotRequired[
        "aws_sdk_notifications.types.notification_configuration_name.NotificationConfigurationName"
    ]
    """<p>The name of the <code>NotificationConfiguration</code>.</p>"""
    description: NotRequired[
        "aws_sdk_notifications.types.notification_configuration_description.NotificationConfigurationDescription"
    ]
    """<p>The description of the <code>NotificationConfiguration</code>.</p>"""
    aggregation_duration: NotRequired[
        "aws_sdk_notifications.types.aggregation_duration.AggregationDuration"
    ]
    """<p>The aggregation preference of the <code>NotificationConfiguration</code>.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>LONG</code> </p> <ul> <li> <p>Aggregate notifications for long periods of time (12 hours).</p> </li> </ul> </li> <li> <p> <code>SHORT</code> </p> <ul> <li> <p>Aggregate notifications for short periods of time (5 minutes).</p> </li> </ul> </li> <li> <p> <code>NONE</code> </p> <ul> <li> <p>Don't aggregate notifications.</p> </li> </ul> </li> </ul> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNotificationConfigurationRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "aggregation_duration" in value:
        out["aggregationDuration"] = value["aggregation_duration"]
    return out


def deserialize_json(data: dict) -> UpdateNotificationConfigurationRequest:
    out: UpdateNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "aggregationDuration" in data:
        out["aggregation_duration"] = data["aggregationDuration"]
    return out
