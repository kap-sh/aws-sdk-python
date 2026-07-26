"""Generated from Smithy shape ``com.amazonaws.imagebuilder#SsmParameterConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.ssm_parameter_configuration

SsmParameterConfigurationList: TypeAlias = list[
    "capo_imagebuilder.types.ssm_parameter_configuration.SsmParameterConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: SsmParameterConfigurationList) -> list:
    import capo_imagebuilder.types.ssm_parameter_configuration

    out: list = []
    for item in value:
        out.append(
            capo_imagebuilder.types.ssm_parameter_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SsmParameterConfigurationList:
    import capo_imagebuilder.types.ssm_parameter_configuration

    out: SsmParameterConfigurationList = []
    for item in data:
        out.append(
            capo_imagebuilder.types.ssm_parameter_configuration.deserialize_json(item)
        )
    return out
