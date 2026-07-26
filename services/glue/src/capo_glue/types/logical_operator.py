"""Generated from Smithy shape ``com.amazonaws.glue#LogicalOperator``."""

from typing import Literal, TypeAlias, cast

LogicalOperator: TypeAlias = Literal["EQUALS",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogicalOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogicalOperator:
    return cast(LogicalOperator, data)
