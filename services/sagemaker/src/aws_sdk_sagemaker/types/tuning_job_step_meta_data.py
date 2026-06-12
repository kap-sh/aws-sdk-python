"""Generated from Smithy shape ``com.amazonaws.sagemaker#TuningJobStepMetaData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_arn


class TuningJobStepMetaData(TypedDict):
    arn: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_tuning_job_arn.HyperParameterTuningJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the tuning job that was run by this step execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TuningJobStepMetaData) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TuningJobStepMetaData:
    out: TuningJobStepMetaData = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
