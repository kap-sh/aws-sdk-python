"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTuningJobStrategyType``."""

from typing import Literal, TypeAlias, cast

"""<p>The strategy hyperparameter tuning uses to find the best combination of hyperparameters for your model. </p>"""
HyperParameterTuningJobStrategyType: TypeAlias = Literal[
    "Bayesian",
    "Random",
    "Hyperband",
    "Grid",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterTuningJobStrategyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HyperParameterTuningJobStrategyType:
    return cast(HyperParameterTuningJobStrategyType, data)
