"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTuningJobObjectiveType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

HyperParameterTuningJobObjectiveType: TypeAlias = Literal[
    "Maximize",
    "Minimize",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Maximize",
        "Minimize",
    )
)


def serialize_aws_json_1_1(value: HyperParameterTuningJobObjectiveType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HyperParameterTuningJobObjectiveType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown HyperParameterTuningJobObjectiveType value: {data!r}"
        )
    return cast(HyperParameterTuningJobObjectiveType, data)
