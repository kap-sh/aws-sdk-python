"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingProgressInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.total_step_count_per_epoch
    import aws_sdk_sagemaker.types.training_epoch_count
    import aws_sdk_sagemaker.types.training_epoch_index
    import aws_sdk_sagemaker.types.training_step_index


class TrainingProgressInfo(TypedDict, closed=True):
    total_step_count_per_epoch: NotRequired[
        "aws_sdk_sagemaker.types.total_step_count_per_epoch.TotalStepCountPerEpoch"
    ]
    """<p> The total step count per epoch. </p>"""
    current_step: NotRequired[
        "aws_sdk_sagemaker.types.training_step_index.TrainingStepIndex"
    ]
    """<p> The current step number. </p>"""
    current_epoch: NotRequired[
        "aws_sdk_sagemaker.types.training_epoch_index.TrainingEpochIndex"
    ]
    """<p> The current epoch number. </p>"""
    max_epoch: NotRequired[
        "aws_sdk_sagemaker.types.training_epoch_count.TrainingEpochCount"
    ]
    """<p> The maximum number of epochs for this job. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingProgressInfo) -> dict:
    out: dict = {}
    if "total_step_count_per_epoch" in value:
        out["TotalStepCountPerEpoch"] = value["total_step_count_per_epoch"]
    if "current_step" in value:
        out["CurrentStep"] = value["current_step"]
    if "current_epoch" in value:
        out["CurrentEpoch"] = value["current_epoch"]
    if "max_epoch" in value:
        out["MaxEpoch"] = value["max_epoch"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingProgressInfo:
    out: TrainingProgressInfo = {}  # type: ignore[typeddict-item]
    if "TotalStepCountPerEpoch" in data:
        out["total_step_count_per_epoch"] = data["TotalStepCountPerEpoch"]
    if "CurrentStep" in data:
        out["current_step"] = data["CurrentStep"]
    if "CurrentEpoch" in data:
        out["current_epoch"] = data["CurrentEpoch"]
    if "MaxEpoch" in data:
        out["max_epoch"] = data["MaxEpoch"]
    return out
