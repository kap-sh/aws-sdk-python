"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#ConfigurationDefinitionsInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_quicksetup.types.configuration_definition_input

ConfigurationDefinitionsInputList: TypeAlias = list[
    "capo_ssm_quicksetup.types.configuration_definition_input.ConfigurationDefinitionInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationDefinitionsInputList) -> list:
    import capo_ssm_quicksetup.types.configuration_definition_input

    out: list = []
    for item in value:
        out.append(
            capo_ssm_quicksetup.types.configuration_definition_input.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConfigurationDefinitionsInputList:
    import capo_ssm_quicksetup.types.configuration_definition_input

    out: ConfigurationDefinitionsInputList = []
    for item in data:
        out.append(
            capo_ssm_quicksetup.types.configuration_definition_input.deserialize_json(
                item
            )
        )
    return out
