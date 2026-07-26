"""Generated from Smithy shape ``com.amazonaws.sagemaker#SecondaryStatusTransitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.secondary_status_transition

SecondaryStatusTransitions: TypeAlias = list[
    "capo_sagemaker.types.secondary_status_transition.SecondaryStatusTransition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecondaryStatusTransitions) -> list:
    import capo_sagemaker.types.secondary_status_transition

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.secondary_status_transition.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SecondaryStatusTransitions:
    import capo_sagemaker.types.secondary_status_transition

    out: SecondaryStatusTransitions = []
    for item in data:
        out.append(
            capo_sagemaker.types.secondary_status_transition.deserialize_aws_json_1_1(
                item
            )
        )
    return out
