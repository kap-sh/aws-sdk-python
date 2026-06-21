"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#Finding``."""

from typing import Literal, TypeAlias, cast

Finding: TypeAlias = Literal[
    "Underprovisioned",
    "Overprovisioned",
    "Optimized",
    "NotOptimized",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Finding) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Finding:
    return cast(Finding, data)
