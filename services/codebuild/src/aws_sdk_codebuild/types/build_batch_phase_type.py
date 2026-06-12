"""Generated from Smithy shape ``com.amazonaws.codebuild#BuildBatchPhaseType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

BuildBatchPhaseType: TypeAlias = Literal[
    "SUBMITTED",
    "DOWNLOAD_BATCHSPEC",
    "IN_PROGRESS",
    "COMBINE_ARTIFACTS",
    "SUCCEEDED",
    "FAILED",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUBMITTED",
        "DOWNLOAD_BATCHSPEC",
        "IN_PROGRESS",
        "COMBINE_ARTIFACTS",
        "SUCCEEDED",
        "FAILED",
        "STOPPED",
    )
)


def serialize_aws_json_1_1(value: BuildBatchPhaseType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BuildBatchPhaseType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BuildBatchPhaseType value: {data!r}")
    return cast(BuildBatchPhaseType, data)
