"""Generated from Smithy shape ``com.amazonaws.costexplorer#Metric``."""

from typing import Literal, TypeAlias, cast

Metric: TypeAlias = Literal[
    "BLENDED_COST",
    "UNBLENDED_COST",
    "AMORTIZED_COST",
    "NET_UNBLENDED_COST",
    "NET_AMORTIZED_COST",
    "USAGE_QUANTITY",
    "NORMALIZED_USAGE_AMOUNT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Metric) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Metric:
    return cast(Metric, data)
