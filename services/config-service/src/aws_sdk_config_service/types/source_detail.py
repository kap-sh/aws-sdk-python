"""Generated from Smithy shape ``com.amazonaws.configservice#SourceDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.event_source
    import aws_sdk_config_service.types.maximum_execution_frequency
    import aws_sdk_config_service.types.message_type


class SourceDetail(TypedDict, closed=True):
    event_source: NotRequired["aws_sdk_config_service.types.event_source.EventSource"]
    """<p>The source of the event, such as an Amazon Web Services service, that triggers Config to evaluate your Amazon Web Services resources.</p>"""
    message_type: NotRequired["aws_sdk_config_service.types.message_type.MessageType"]
    """<p>The type of notification that triggers Config to run an evaluation for a rule. You can specify the following notification types:</p> <ul> <li> <p> <code>ConfigurationItemChangeNotification</code> - Triggers an evaluation when Config delivers a configuration item as a result of a resource change.</p> </li> <li> <p> <code>OversizedConfigurationItemChangeNotification</code> - Triggers an evaluation when Config delivers an oversized configuration item. Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS.</p> </li> <li> <p> <code>ScheduledNotification</code> - Triggers a periodic evaluation at the frequency specified for <code>MaximumExecutionFrequency</code>.</p> </li> <li> <p> <code>ConfigurationSnapshotDeliveryCompleted</code> - Triggers a periodic evaluation when Config delivers a configuration snapshot.</p> </li> </ul> <p>If you want your custom rule to be triggered by configuration changes, specify two SourceDetail objects, one for <code>ConfigurationItemChangeNotification</code> and one for <code>OversizedConfigurationItemChangeNotification</code>.</p>"""
    maximum_execution_frequency: NotRequired[
        "aws_sdk_config_service.types.maximum_execution_frequency.MaximumExecutionFrequency"
    ]
    """<p>The frequency at which you want Config to run evaluations for a custom rule with a periodic trigger. If you specify a value for <code>MaximumExecutionFrequency</code>, then <code>MessageType</code> must use the <code>ScheduledNotification</code> value.</p> <note> <p>By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the <code>MaximumExecutionFrequency</code> parameter.</p> <p>Based on the valid value you choose, Config runs evaluations once for each valid value. For example, if you choose <code>Three_Hours</code>, Config runs evaluations once every three hours. In this case, <code>Three_Hours</code> is the frequency of this rule. </p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceDetail) -> dict:
    out: dict = {}
    if "event_source" in value:
        import aws_sdk_config_service.types.event_source

        out["EventSource"] = (
            aws_sdk_config_service.types.event_source.serialize_aws_json_1_1(
                value["event_source"]
            )
        )
    if "message_type" in value:
        import aws_sdk_config_service.types.message_type

        out["MessageType"] = (
            aws_sdk_config_service.types.message_type.serialize_aws_json_1_1(
                value["message_type"]
            )
        )
    if "maximum_execution_frequency" in value:
        import aws_sdk_config_service.types.maximum_execution_frequency

        out["MaximumExecutionFrequency"] = (
            aws_sdk_config_service.types.maximum_execution_frequency.serialize_aws_json_1_1(
                value["maximum_execution_frequency"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceDetail:
    out: SourceDetail = {}  # type: ignore[typeddict-item]
    if "EventSource" in data:
        import aws_sdk_config_service.types.event_source

        out["event_source"] = (
            aws_sdk_config_service.types.event_source.deserialize_aws_json_1_1(
                data["EventSource"]
            )
        )
    if "MessageType" in data:
        import aws_sdk_config_service.types.message_type

        out["message_type"] = (
            aws_sdk_config_service.types.message_type.deserialize_aws_json_1_1(
                data["MessageType"]
            )
        )
    if "MaximumExecutionFrequency" in data:
        import aws_sdk_config_service.types.maximum_execution_frequency

        out["maximum_execution_frequency"] = (
            aws_sdk_config_service.types.maximum_execution_frequency.deserialize_aws_json_1_1(
                data["MaximumExecutionFrequency"]
            )
        )
    return out
