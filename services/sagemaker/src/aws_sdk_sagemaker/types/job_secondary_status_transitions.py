"""Generated from Smithy shape ``com.amazonaws.sagemaker#JobSecondaryStatusTransitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.job_secondary_status_transition

JobSecondaryStatusTransitions: TypeAlias = list[
    "aws_sdk_sagemaker.types.job_secondary_status_transition.JobSecondaryStatusTransition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobSecondaryStatusTransitions) -> list:
    import aws_sdk_sagemaker.types.job_secondary_status_transition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.job_secondary_status_transition.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> JobSecondaryStatusTransitions:
    import aws_sdk_sagemaker.types.job_secondary_status_transition

    out: JobSecondaryStatusTransitions = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.job_secondary_status_transition.deserialize_aws_json_1_1(
                item
            )
        )
    return out
