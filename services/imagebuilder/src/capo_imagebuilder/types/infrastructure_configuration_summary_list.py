"""Generated from Smithy shape ``com.amazonaws.imagebuilder#InfrastructureConfigurationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.infrastructure_configuration_summary

InfrastructureConfigurationSummaryList: TypeAlias = list[
    "capo_imagebuilder.types.infrastructure_configuration_summary.InfrastructureConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: InfrastructureConfigurationSummaryList) -> list:
    import capo_imagebuilder.types.infrastructure_configuration_summary

    out: list = []
    for item in value:
        out.append(
            capo_imagebuilder.types.infrastructure_configuration_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> InfrastructureConfigurationSummaryList:
    import capo_imagebuilder.types.infrastructure_configuration_summary

    out: InfrastructureConfigurationSummaryList = []
    for item in data:
        out.append(
            capo_imagebuilder.types.infrastructure_configuration_summary.deserialize_json(
                item
            )
        )
    return out
