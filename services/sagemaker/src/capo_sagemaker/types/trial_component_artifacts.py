"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrialComponentArtifacts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.trial_component_artifact
    import capo_sagemaker.types.trial_component_key128

TrialComponentArtifacts: TypeAlias = dict[
    "capo_sagemaker.types.trial_component_key128.TrialComponentKey128",
    "capo_sagemaker.types.trial_component_artifact.TrialComponentArtifact",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: TrialComponentArtifacts) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_sagemaker.types.trial_component_artifact

        out[key] = capo_sagemaker.types.trial_component_artifact.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrialComponentArtifacts:
    out: TrialComponentArtifacts = {}
    for key, value in data.items():
        import capo_sagemaker.types.trial_component_artifact

        out[key] = (
            capo_sagemaker.types.trial_component_artifact.deserialize_aws_json_1_1(
                value
            )
        )
    return out
