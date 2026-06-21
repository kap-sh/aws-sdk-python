"""Generated from Smithy shape ``com.amazonaws.sagemaker#AggregationTransformationValue``."""

from typing import Literal, TypeAlias, cast

AggregationTransformationValue: TypeAlias = Literal[
    "sum",
    "avg",
    "first",
    "min",
    "max",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregationTransformationValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AggregationTransformationValue:
    return cast(AggregationTransformationValue, data)
