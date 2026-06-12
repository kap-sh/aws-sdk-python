"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTuningJobStrategyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

"""<p>The strategy hyperparameter tuning uses to find the best combination of hyperparameters for your model. </p>"""
HyperParameterTuningJobStrategyType: TypeAlias = Literal[
    "Bayesian",
    "Random",
    "Hyperband",
    "Grid",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Bayesian",
        "Random",
        "Hyperband",
        "Grid",
    )
)


def serialize_aws_json_1_1(value: HyperParameterTuningJobStrategyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HyperParameterTuningJobStrategyType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown HyperParameterTuningJobStrategyType value: {data!r}"
        )
    return cast(HyperParameterTuningJobStrategyType, data)
