"""Generated from Smithy shape ``com.amazonaws.glue#AggFunction``."""

from typing import Literal, TypeAlias, cast

AggFunction: TypeAlias = Literal[
    "avg",
    "countDistinct",
    "count",
    "first",
    "last",
    "kurtosis",
    "max",
    "min",
    "skewness",
    "stddev_samp",
    "stddev_pop",
    "sum",
    "sumDistinct",
    "var_samp",
    "var_pop",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggFunction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AggFunction:
    return cast(AggFunction, data)
