"""Generated from Smithy shape ``com.amazonaws.sagemaker#StageStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

StageStatus: TypeAlias = Literal[
    "CREATING",
    "READYTODEPLOY",
    "STARTING",
    "INPROGRESS",
    "DEPLOYED",
    "FAILED",
    "STOPPING",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "READYTODEPLOY",
        "STARTING",
        "INPROGRESS",
        "DEPLOYED",
        "FAILED",
        "STOPPING",
        "STOPPED",
    )
)


def serialize_aws_json_1_1(value: StageStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StageStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StageStatus value: {data!r}")
    return cast(StageStatus, data)
