"""Generated from Smithy shape ``com.amazonaws.sagemaker#SecondaryStatus``."""

from typing import Literal, TypeAlias, cast

SecondaryStatus: TypeAlias = Literal[
    "Starting",
    "LaunchingMLInstances",
    "PreparingTrainingStack",
    "Downloading",
    "DownloadingTrainingImage",
    "Training",
    "Uploading",
    "Stopping",
    "Stopped",
    "MaxRuntimeExceeded",
    "Completed",
    "Failed",
    "Interrupted",
    "MaxWaitTimeExceeded",
    "Updating",
    "Restarting",
    "Pending",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecondaryStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SecondaryStatus:
    return cast(SecondaryStatus, data)
