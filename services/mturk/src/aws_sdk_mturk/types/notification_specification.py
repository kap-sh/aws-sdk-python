"""Generated from Smithy shape ``com.amazonaws.mturk#NotificationSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mturk.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mturk.types.event_type_list
    import aws_sdk_mturk.types.notification_transport
    import aws_sdk_mturk.types.string


class NotificationSpecification(TypedDict, closed=True):
    destination: "aws_sdk_mturk.types.string.String"
    """<p> The target for notification messages. The Destination’s format is determined by the specified Transport: </p> <ul> <li> <p>When Transport is Email, the Destination is your email address.</p> </li> <li> <p>When Transport is SQS, the Destination is your queue URL.</p> </li> <li> <p>When Transport is SNS, the Destination is the ARN of your topic.</p> </li> </ul>"""
    transport: "aws_sdk_mturk.types.notification_transport.NotificationTransport"
    """<p> The method Amazon Mechanical Turk uses to send the notification. Valid Values: Email | SQS | SNS. </p>"""
    version: "aws_sdk_mturk.types.string.String"
    """<p>The version of the Notification API to use. Valid value is 2006-05-05.</p>"""
    event_types: "aws_sdk_mturk.types.event_type_list.EventTypeList"
    """<p> The list of events that should cause notifications to be sent. Valid Values: AssignmentAccepted | AssignmentAbandoned | AssignmentReturned | AssignmentSubmitted | AssignmentRejected | AssignmentApproved | HITCreated | HITExtended | HITDisposed | HITReviewable | HITExpired | Ping. The Ping event is only valid for the SendTestEventNotification operation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotificationSpecification) -> dict:
    out: dict = {}
    out["Destination"] = value["destination"]
    import aws_sdk_mturk.types.notification_transport

    out["Transport"] = (
        aws_sdk_mturk.types.notification_transport.serialize_aws_json_1_1(
            value["transport"]
        )
    )
    out["Version"] = value["version"]
    import aws_sdk_mturk.types.event_type_list

    out["EventTypes"] = aws_sdk_mturk.types.event_type_list.serialize_aws_json_1_1(
        value["event_types"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> NotificationSpecification:
    out: NotificationSpecification = {}  # type: ignore[typeddict-item]
    if "Destination" in data:
        out["destination"] = data["Destination"]
    else:
        raise DeserializationError("NotificationSpecification.destination required")
    if "Transport" in data:
        import aws_sdk_mturk.types.notification_transport

        out["transport"] = (
            aws_sdk_mturk.types.notification_transport.deserialize_aws_json_1_1(
                data["Transport"]
            )
        )
    else:
        raise DeserializationError("NotificationSpecification.transport required")
    if "Version" in data:
        out["version"] = data["Version"]
    else:
        raise DeserializationError("NotificationSpecification.version required")
    if "EventTypes" in data:
        import aws_sdk_mturk.types.event_type_list

        out["event_types"] = (
            aws_sdk_mturk.types.event_type_list.deserialize_aws_json_1_1(
                data["EventTypes"]
            )
        )
    else:
        raise DeserializationError("NotificationSpecification.event_types required")
    return out
