"""Generated from Smithy shape ``com.amazonaws.glue#TriggerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.trigger

TriggerList: TypeAlias = list["aws_sdk_glue.types.trigger.Trigger"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TriggerList) -> list:
    import aws_sdk_glue.types.trigger

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.trigger.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TriggerList:
    import aws_sdk_glue.types.trigger

    out: TriggerList = []
    for item in data:
        out.append(aws_sdk_glue.types.trigger.deserialize_aws_json_1_1(item))
    return out
