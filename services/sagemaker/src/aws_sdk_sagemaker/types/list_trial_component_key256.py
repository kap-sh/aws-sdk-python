"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListTrialComponentKey256``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.trial_component_key256

ListTrialComponentKey256: TypeAlias = list[
    "aws_sdk_sagemaker.types.trial_component_key256.TrialComponentKey256"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTrialComponentKey256) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ListTrialComponentKey256:
    return list(data)
