"""Generated from Smithy shape ``com.amazonaws.glue#AggFunction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_aws_json_1_1(value: AggFunction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AggFunction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AggFunction value: {data!r}")
    return cast(AggFunction, data)
