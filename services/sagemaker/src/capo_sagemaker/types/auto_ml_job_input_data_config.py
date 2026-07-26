"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLJobInputDataConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_job_channel

AutoMLJobInputDataConfig: TypeAlias = list[
    "capo_sagemaker.types.auto_ml_job_channel.AutoMLJobChannel"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLJobInputDataConfig) -> list:
    import capo_sagemaker.types.auto_ml_job_channel

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.auto_ml_job_channel.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AutoMLJobInputDataConfig:
    import capo_sagemaker.types.auto_ml_job_channel

    out: AutoMLJobInputDataConfig = []
    for item in data:
        out.append(
            capo_sagemaker.types.auto_ml_job_channel.deserialize_aws_json_1_1(item)
        )
    return out
