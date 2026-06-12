"""Generated from Smithy shape ``com.amazonaws.configservice#RemediationParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.remediation_parameter_value
    import aws_sdk_config_service.types.string_with_char_limit256

RemediationParameters: TypeAlias = dict[
    "aws_sdk_config_service.types.string_with_char_limit256.StringWithCharLimit256",
    "aws_sdk_config_service.types.remediation_parameter_value.RemediationParameterValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: RemediationParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_config_service.types.remediation_parameter_value

        out[key] = (
            aws_sdk_config_service.types.remediation_parameter_value.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RemediationParameters:
    out: RemediationParameters = {}
    for key, value in data.items():
        import aws_sdk_config_service.types.remediation_parameter_value

        out[key] = (
            aws_sdk_config_service.types.remediation_parameter_value.deserialize_aws_json_1_1(
                value
            )
        )
    return out
