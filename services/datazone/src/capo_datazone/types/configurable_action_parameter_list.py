"""Generated from Smithy shape ``com.amazonaws.datazone#ConfigurableActionParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.configurable_action_parameter

ConfigurableActionParameterList: TypeAlias = list[
    "capo_datazone.types.configurable_action_parameter.ConfigurableActionParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurableActionParameterList) -> list:
    import capo_datazone.types.configurable_action_parameter

    out: list = []
    for item in value:
        out.append(
            capo_datazone.types.configurable_action_parameter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ConfigurableActionParameterList:
    import capo_datazone.types.configurable_action_parameter

    out: ConfigurableActionParameterList = []
    for item in data:
        out.append(
            capo_datazone.types.configurable_action_parameter.deserialize_json(item)
        )
    return out
