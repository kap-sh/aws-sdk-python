"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#ConfigurationDefinitionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_quicksetup.types.configuration_definition

ConfigurationDefinitionsList: TypeAlias = list[
    "capo_ssm_quicksetup.types.configuration_definition.ConfigurationDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationDefinitionsList) -> list:
    import capo_ssm_quicksetup.types.configuration_definition

    out: list = []
    for item in value:
        out.append(
            capo_ssm_quicksetup.types.configuration_definition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ConfigurationDefinitionsList:
    import capo_ssm_quicksetup.types.configuration_definition

    out: ConfigurationDefinitionsList = []
    for item in data:
        out.append(
            capo_ssm_quicksetup.types.configuration_definition.deserialize_json(item)
        )
    return out
