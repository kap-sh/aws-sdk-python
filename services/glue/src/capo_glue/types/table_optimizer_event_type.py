"""Generated from Smithy shape ``com.amazonaws.glue#TableOptimizerEventType``."""

from typing import Literal, TypeAlias, cast

TableOptimizerEventType: TypeAlias = Literal[
    "starting",
    "completed",
    "failed",
    "in_progress",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableOptimizerEventType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TableOptimizerEventType:
    return cast(TableOptimizerEventType, data)
