"""Generated from Smithy shape ``com.amazonaws.glue#ActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.action

ActionList: TypeAlias = list["capo_glue.types.action.Action"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionList) -> list:
    import capo_glue.types.action

    out: list = []
    for item in value:
        out.append(capo_glue.types.action.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ActionList:
    import capo_glue.types.action

    out: ActionList = []
    for item in data:
        out.append(capo_glue.types.action.deserialize_aws_json_1_1(item))
    return out
