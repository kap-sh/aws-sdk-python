"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#Source``."""

from typing import Literal, TypeAlias, cast

Source: TypeAlias = Literal[
    "ComputeOptimizer",
    "CostExplorer",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Source) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Source:
    return cast(Source, data)
