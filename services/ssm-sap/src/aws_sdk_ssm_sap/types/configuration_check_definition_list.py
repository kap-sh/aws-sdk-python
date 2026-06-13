"""Generated from Smithy shape ``com.amazonaws.ssmsap#ConfigurationCheckDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.configuration_check_definition

ConfigurationCheckDefinitionList: TypeAlias = list[
    "aws_sdk_ssm_sap.types.configuration_check_definition.ConfigurationCheckDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationCheckDefinitionList) -> list:
    import aws_sdk_ssm_sap.types.configuration_check_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm_sap.types.configuration_check_definition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ConfigurationCheckDefinitionList:
    import aws_sdk_ssm_sap.types.configuration_check_definition

    out: ConfigurationCheckDefinitionList = []
    for item in data:
        out.append(
            aws_sdk_ssm_sap.types.configuration_check_definition.deserialize_json(item)
        )
    return out
