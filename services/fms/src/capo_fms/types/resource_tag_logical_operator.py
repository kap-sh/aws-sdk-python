"""Generated from Smithy shape ``com.amazonaws.fms#ResourceTagLogicalOperator``."""

from typing import Literal, TypeAlias, cast

ResourceTagLogicalOperator: TypeAlias = Literal[
    "AND",
    "OR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceTagLogicalOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceTagLogicalOperator:
    return cast(ResourceTagLogicalOperator, data)
