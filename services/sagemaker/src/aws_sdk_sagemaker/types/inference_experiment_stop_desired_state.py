"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceExperimentStopDesiredState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

InferenceExperimentStopDesiredState: TypeAlias = Literal[
    "Completed",
    "Cancelled",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Completed",
        "Cancelled",
    )
)


def serialize_aws_json_1_1(value: InferenceExperimentStopDesiredState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InferenceExperimentStopDesiredState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InferenceExperimentStopDesiredState value: {data!r}"
        )
    return cast(InferenceExperimentStopDesiredState, data)
