"""Generated from Smithy shape ``com.amazonaws.codedeploy#TriggerEventTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.trigger_event_type

TriggerEventTypeList: TypeAlias = list[
    "aws_sdk_codedeploy.types.trigger_event_type.TriggerEventType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TriggerEventTypeList) -> list:
    import aws_sdk_codedeploy.types.trigger_event_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codedeploy.types.trigger_event_type.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TriggerEventTypeList:
    import aws_sdk_codedeploy.types.trigger_event_type

    out: TriggerEventTypeList = []
    for item in data:
        out.append(
            aws_sdk_codedeploy.types.trigger_event_type.deserialize_aws_json_1_1(item)
        )
    return out
