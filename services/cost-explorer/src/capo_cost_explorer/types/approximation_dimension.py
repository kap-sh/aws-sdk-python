"""Generated from Smithy shape ``com.amazonaws.costexplorer#ApproximationDimension``."""

from typing import Literal, TypeAlias, cast

ApproximationDimension: TypeAlias = Literal[
    "SERVICE",
    "RESOURCE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApproximationDimension) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApproximationDimension:
    return cast(ApproximationDimension, data)
