"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.configurable_environment_action

EnvironmentActionList: TypeAlias = list[
    "capo_datazone.types.configurable_environment_action.ConfigurableEnvironmentAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentActionList) -> list:
    import capo_datazone.types.configurable_environment_action

    out: list = []
    for item in value:
        out.append(
            capo_datazone.types.configurable_environment_action.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EnvironmentActionList:
    import capo_datazone.types.configurable_environment_action

    out: EnvironmentActionList = []
    for item in data:
        out.append(
            capo_datazone.types.configurable_environment_action.deserialize_json(item)
        )
    return out
