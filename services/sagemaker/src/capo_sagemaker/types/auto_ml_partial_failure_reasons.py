"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLPartialFailureReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_partial_failure_reason

AutoMLPartialFailureReasons: TypeAlias = list[
    "capo_sagemaker.types.auto_ml_partial_failure_reason.AutoMLPartialFailureReason"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLPartialFailureReasons) -> list:
    import capo_sagemaker.types.auto_ml_partial_failure_reason

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.auto_ml_partial_failure_reason.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AutoMLPartialFailureReasons:
    import capo_sagemaker.types.auto_ml_partial_failure_reason

    out: AutoMLPartialFailureReasons = []
    for item in data:
        out.append(
            capo_sagemaker.types.auto_ml_partial_failure_reason.deserialize_aws_json_1_1(
                item
            )
        )
    return out
