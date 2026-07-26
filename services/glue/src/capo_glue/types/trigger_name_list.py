"""Generated from Smithy shape ``com.amazonaws.glue#TriggerNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.name_string

TriggerNameList: TypeAlias = list["capo_glue.types.name_string.NameString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TriggerNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TriggerNameList:
    return list(data)
