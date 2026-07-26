"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentBlueprintConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.environment_blueprint_configuration_item

EnvironmentBlueprintConfigurations: TypeAlias = list[
    "capo_datazone.types.environment_blueprint_configuration_item.EnvironmentBlueprintConfigurationItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentBlueprintConfigurations) -> list:
    import capo_datazone.types.environment_blueprint_configuration_item

    out: list = []
    for item in value:
        out.append(
            capo_datazone.types.environment_blueprint_configuration_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EnvironmentBlueprintConfigurations:
    import capo_datazone.types.environment_blueprint_configuration_item

    out: EnvironmentBlueprintConfigurations = []
    for item in data:
        out.append(
            capo_datazone.types.environment_blueprint_configuration_item.deserialize_json(
                item
            )
        )
    return out
