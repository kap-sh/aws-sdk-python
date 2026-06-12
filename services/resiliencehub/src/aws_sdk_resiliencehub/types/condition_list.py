"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.condition

ConditionList: TypeAlias = list["aws_sdk_resiliencehub.types.condition.Condition"]


# --- restJson1 ser/de ---
def serialize_json(value: ConditionList) -> list:
    import aws_sdk_resiliencehub.types.condition

    out: list = []
    for item in value:
        out.append(aws_sdk_resiliencehub.types.condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConditionList:
    import aws_sdk_resiliencehub.types.condition

    out: ConditionList = []
    for item in data:
        out.append(aws_sdk_resiliencehub.types.condition.deserialize_json(item))
    return out
