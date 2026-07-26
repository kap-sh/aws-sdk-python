"""Generated from Smithy shape ``com.amazonaws.emrcontainers#TemplateParameterConfigurationMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr_containers.types.template_parameter_configuration
    import capo_emr_containers.types.template_parameter_name

TemplateParameterConfigurationMap: TypeAlias = dict[
    "capo_emr_containers.types.template_parameter_name.TemplateParameterName",
    "capo_emr_containers.types.template_parameter_configuration.TemplateParameterConfiguration",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TemplateParameterConfigurationMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_emr_containers.types.template_parameter_configuration

        out[key] = (
            capo_emr_containers.types.template_parameter_configuration.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> TemplateParameterConfigurationMap:
    out: TemplateParameterConfigurationMap = {}
    for key, value in data.items():
        import capo_emr_containers.types.template_parameter_configuration

        out[key] = (
            capo_emr_containers.types.template_parameter_configuration.deserialize_json(
                value
            )
        )
    return out
