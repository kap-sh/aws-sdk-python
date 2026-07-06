"""Generated from Smithy shape ``com.amazonaws.resiliencehub#EventSubscription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.arn
    import aws_sdk_resiliencehub.types.event_type
    import aws_sdk_resiliencehub.types.string255


class EventSubscription(TypedDict, closed=True):
    name: "aws_sdk_resiliencehub.types.string255.String255"
    """<p>Unique name to identify an event subscription.</p>"""
    event_type: "aws_sdk_resiliencehub.types.event_type.EventType"
    """<p>The type of event you would like to subscribe and get notification for. Currently, Resilience Hub supports notifications only for <b>Drift detected</b> (<code>DriftDetected</code>) and <b>Scheduled assessment failure</b> (<code>ScheduledAssessmentFailure</code>) events.</p>"""
    sns_topic_arn: NotRequired["aws_sdk_resiliencehub.types.arn.Arn"]
    r"""<p>Amazon Resource Name (ARN) of the Amazon Simple Notification Service topic. The format for this ARN is: <code>arn:partition:sns:region:account:topic-name</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventSubscription) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_resiliencehub.types.event_type

    out["eventType"] = aws_sdk_resiliencehub.types.event_type.serialize_json(
        value["event_type"]
    )
    if "sns_topic_arn" in value:
        out["snsTopicArn"] = value["sns_topic_arn"]
    return out


def deserialize_json(data: dict) -> EventSubscription:
    out: EventSubscription = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("EventSubscription.name required")
    if "eventType" in data:
        import aws_sdk_resiliencehub.types.event_type

        out["event_type"] = aws_sdk_resiliencehub.types.event_type.deserialize_json(
            data["eventType"]
        )
    else:
        raise DeserializationError("EventSubscription.event_type required")
    if "snsTopicArn" in data:
        out["sns_topic_arn"] = data["snsTopicArn"]
    return out
