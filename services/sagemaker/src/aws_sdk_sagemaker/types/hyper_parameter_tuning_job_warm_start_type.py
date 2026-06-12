"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTuningJobWarmStartType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

HyperParameterTuningJobWarmStartType: TypeAlias = Literal[
    "IdenticalDataAndAlgorithm",
    "TransferLearning",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IdenticalDataAndAlgorithm",
        "TransferLearning",
    )
)


def serialize_aws_json_1_1(value: HyperParameterTuningJobWarmStartType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HyperParameterTuningJobWarmStartType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown HyperParameterTuningJobWarmStartType value: {data!r}"
        )
    return cast(HyperParameterTuningJobWarmStartType, data)
