"""Generated from Smithy shape ``com.amazonaws.glue#TriggerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.trigger

TriggerList: TypeAlias = list["capo_glue.types.trigger.Trigger"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TriggerList) -> list:
    import capo_glue.types.trigger

    out: list = []
    for item in value:
        out.append(capo_glue.types.trigger.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TriggerList:
    import capo_glue.types.trigger

    out: TriggerList = []
    for item in data:
        out.append(capo_glue.types.trigger.deserialize_aws_json_1_1(item))
    return out
