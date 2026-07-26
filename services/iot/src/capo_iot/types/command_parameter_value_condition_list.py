"""Generated from Smithy shape ``com.amazonaws.iot#CommandParameterValueConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.command_parameter_value_condition

CommandParameterValueConditionList: TypeAlias = list[
    "capo_iot.types.command_parameter_value_condition.CommandParameterValueCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: CommandParameterValueConditionList) -> list:
    import capo_iot.types.command_parameter_value_condition

    out: list = []
    for item in value:
        out.append(
            capo_iot.types.command_parameter_value_condition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CommandParameterValueConditionList:
    import capo_iot.types.command_parameter_value_condition

    out: CommandParameterValueConditionList = []
    for item in data:
        out.append(
            capo_iot.types.command_parameter_value_condition.deserialize_json(item)
        )
    return out
