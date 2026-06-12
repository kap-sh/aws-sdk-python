"""Generated from Smithy shape ``com.amazonaws.sagemaker#SecondaryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_aws_json_1_1(value: SecondaryStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SecondaryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SecondaryStatus value: {data!r}")
    return cast(SecondaryStatus, data)
