"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#TemplateVariablesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.template_variable_metadata

TemplateVariablesMap: TypeAlias = dict[
    "str",
    "aws_sdk_pinpoint_sms_voice_v2.types.template_variable_metadata.TemplateVariableMetadata",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: TemplateVariablesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_pinpoint_sms_voice_v2.types.template_variable_metadata

        out[key] = (
            aws_sdk_pinpoint_sms_voice_v2.types.template_variable_metadata.serialize_aws_json_1_0(
                value
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TemplateVariablesMap:
    out: TemplateVariablesMap = {}
    for key, value in data.items():
        import aws_sdk_pinpoint_sms_voice_v2.types.template_variable_metadata

        out[key] = (
            aws_sdk_pinpoint_sms_voice_v2.types.template_variable_metadata.deserialize_aws_json_1_0(
                value
            )
        )
    return out
