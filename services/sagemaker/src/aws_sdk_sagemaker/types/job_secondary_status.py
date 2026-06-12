"""Generated from Smithy shape ``com.amazonaws.sagemaker#JobSecondaryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

JobSecondaryStatus: TypeAlias = Literal[
    "Starting",
    "Downloading",
    "Training",
    "Uploading",
    "Stopping",
    "Stopped",
    "MaxRuntimeExceeded",
    "Interrupted",
    "Failed",
    "Completed",
    "Restarting",
    "Pending",
    "Evaluating",
    "Deleting",
    "DeleteFailed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Starting",
        "Downloading",
        "Training",
        "Uploading",
        "Stopping",
        "Stopped",
        "MaxRuntimeExceeded",
        "Interrupted",
        "Failed",
        "Completed",
        "Restarting",
        "Pending",
        "Evaluating",
        "Deleting",
        "DeleteFailed",
    )
)


def serialize_aws_json_1_1(value: JobSecondaryStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JobSecondaryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobSecondaryStatus value: {data!r}")
    return cast(JobSecondaryStatus, data)
