"""Generated from Smithy shape ``com.amazonaws.emrcontainers#TemplateParameterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.string1024
    import capo_emr_containers.types.template_parameter_data_type


class TemplateParameterConfiguration(TypedDict, closed=True):
    type: NotRequired[
        "capo_emr_containers.types.template_parameter_data_type.TemplateParameterDataType"
    ]
    """<p>The type of the job template parameter. Allowed values are: ‘STRING’, ‘NUMBER’.</p>"""
    default_value: NotRequired["capo_emr_containers.types.string1024.String1024"]
    """<p>The default value for the job template parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateParameterConfiguration) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_emr_containers.types.template_parameter_data_type

        out["type"] = (
            capo_emr_containers.types.template_parameter_data_type.serialize_json(
                value["type"]
            )
        )
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    return out


def deserialize_json(data: dict) -> TemplateParameterConfiguration:
    out: TemplateParameterConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import capo_emr_containers.types.template_parameter_data_type

        out["type"] = (
            capo_emr_containers.types.template_parameter_data_type.deserialize_json(
                data["type"]
            )
        )
    if "defaultValue" in data:
        out["default_value"] = data["defaultValue"]
    return out
