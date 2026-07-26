"""Generated from Smithy shape ``com.amazonaws.emrcontainers#TemplateParameterInputMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr_containers.types.string1024
    import capo_emr_containers.types.template_parameter_name

TemplateParameterInputMap: TypeAlias = dict[
    "capo_emr_containers.types.template_parameter_name.TemplateParameterName",
    "capo_emr_containers.types.string1024.String1024",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TemplateParameterInputMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> TemplateParameterInputMap:
    out: TemplateParameterInputMap = {}
    for key, value in data.items():
        out[key] = value
    return out
