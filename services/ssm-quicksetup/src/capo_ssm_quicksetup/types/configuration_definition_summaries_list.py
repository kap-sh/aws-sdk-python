"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#ConfigurationDefinitionSummariesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_quicksetup.types.configuration_definition_summary

ConfigurationDefinitionSummariesList: TypeAlias = list[
    "capo_ssm_quicksetup.types.configuration_definition_summary.ConfigurationDefinitionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationDefinitionSummariesList) -> list:
    import capo_ssm_quicksetup.types.configuration_definition_summary

    out: list = []
    for item in value:
        out.append(
            capo_ssm_quicksetup.types.configuration_definition_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConfigurationDefinitionSummariesList:
    import capo_ssm_quicksetup.types.configuration_definition_summary

    out: ConfigurationDefinitionSummariesList = []
    for item in data:
        out.append(
            capo_ssm_quicksetup.types.configuration_definition_summary.deserialize_json(
                item
            )
        )
    return out
