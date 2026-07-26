"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#TemplateVariableSubstitutionMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.template_variable_name
    import capo_pinpoint_sms_voice_v2.types.template_variable_value

TemplateVariableSubstitutionMap: TypeAlias = dict[
    "capo_pinpoint_sms_voice_v2.types.template_variable_name.TemplateVariableName",
    "capo_pinpoint_sms_voice_v2.types.template_variable_value.TemplateVariableValue",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: TemplateVariableSubstitutionMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> TemplateVariableSubstitutionMap:
    out: TemplateVariableSubstitutionMap = {}
    for key, value in data.items():
        out[key] = value
    return out
