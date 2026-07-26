"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrialComponentSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.trial_component_source

TrialComponentSources: TypeAlias = list[
    "capo_sagemaker.types.trial_component_source.TrialComponentSource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrialComponentSources) -> list:
    import capo_sagemaker.types.trial_component_source

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.trial_component_source.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TrialComponentSources:
    import capo_sagemaker.types.trial_component_source

    out: TrialComponentSources = []
    for item in data:
        out.append(
            capo_sagemaker.types.trial_component_source.deserialize_aws_json_1_1(item)
        )
    return out
