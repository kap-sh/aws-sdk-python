"""Generated from Smithy shape ``com.amazonaws.codedeploy#TriggerConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.trigger_event_type_list
    import aws_sdk_codedeploy.types.trigger_name
    import aws_sdk_codedeploy.types.trigger_target_arn


class TriggerConfig(TypedDict):
    trigger_name: NotRequired["aws_sdk_codedeploy.types.trigger_name.TriggerName"]
    """<p>The name of the notification trigger.</p>"""
    trigger_target_arn: NotRequired[
        "aws_sdk_codedeploy.types.trigger_target_arn.TriggerTargetArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon Simple Notification Service topic through which notifications about deployment or instance events are sent.</p>"""
    trigger_events: NotRequired[
        "aws_sdk_codedeploy.types.trigger_event_type_list.TriggerEventTypeList"
    ]
    """<p>The event type or types for which notifications are triggered.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TriggerConfig) -> dict:
    out: dict = {}
    if "trigger_name" in value:
        out["triggerName"] = value["trigger_name"]
    if "trigger_target_arn" in value:
        out["triggerTargetArn"] = value["trigger_target_arn"]
    if "trigger_events" in value:
        import aws_sdk_codedeploy.types.trigger_event_type_list

        out["triggerEvents"] = (
            aws_sdk_codedeploy.types.trigger_event_type_list.serialize_aws_json_1_1(
                value["trigger_events"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TriggerConfig:
    out: TriggerConfig = {}  # type: ignore[typeddict-item]
    if "triggerName" in data:
        out["trigger_name"] = data["triggerName"]
    if "triggerTargetArn" in data:
        out["trigger_target_arn"] = data["triggerTargetArn"]
    if "triggerEvents" in data:
        import aws_sdk_codedeploy.types.trigger_event_type_list

        out["trigger_events"] = (
            aws_sdk_codedeploy.types.trigger_event_type_list.deserialize_aws_json_1_1(
                data["triggerEvents"]
            )
        )
    return out
