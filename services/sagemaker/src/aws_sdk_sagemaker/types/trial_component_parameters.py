"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrialComponentParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.trial_component_key320
    import aws_sdk_sagemaker.types.trial_component_parameter_value

TrialComponentParameters: TypeAlias = dict[
    "aws_sdk_sagemaker.types.trial_component_key320.TrialComponentKey320",
    "aws_sdk_sagemaker.types.trial_component_parameter_value.TrialComponentParameterValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: TrialComponentParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_sagemaker.types.trial_component_parameter_value

        out[key] = (
            aws_sdk_sagemaker.types.trial_component_parameter_value.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrialComponentParameters:
    out: TrialComponentParameters = {}
    for key, value in data.items():
        import aws_sdk_sagemaker.types.trial_component_parameter_value

        out[key] = (
            aws_sdk_sagemaker.types.trial_component_parameter_value.deserialize_aws_json_1_1(
                value
            )
        )
    return out
