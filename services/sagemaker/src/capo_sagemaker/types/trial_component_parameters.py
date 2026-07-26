"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrialComponentParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.trial_component_key320
    import capo_sagemaker.types.trial_component_parameter_value

TrialComponentParameters: TypeAlias = dict[
    "capo_sagemaker.types.trial_component_key320.TrialComponentKey320",
    "capo_sagemaker.types.trial_component_parameter_value.TrialComponentParameterValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: TrialComponentParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_sagemaker.types.trial_component_parameter_value

        out[key] = (
            capo_sagemaker.types.trial_component_parameter_value.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrialComponentParameters:
    out: TrialComponentParameters = {}
    for key, value in data.items():
        import capo_sagemaker.types.trial_component_parameter_value

        out[key] = (
            capo_sagemaker.types.trial_component_parameter_value.deserialize_aws_json_1_1(
                value
            )
        )
    return out
