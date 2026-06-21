"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#EBSFinding``."""

from typing import Literal, TypeAlias, cast

EBSFinding: TypeAlias = Literal[
    "Optimized",
    "NotOptimized",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EBSFinding) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EBSFinding:
    return cast(EBSFinding, data)
