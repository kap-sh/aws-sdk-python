"""Generated from Smithy shape ``com.amazonaws.glue#MaterializedViewRefreshState``."""

from typing import Literal, TypeAlias, cast

MaterializedViewRefreshState: TypeAlias = Literal[
    "STARTING",
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaterializedViewRefreshState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MaterializedViewRefreshState:
    return cast(MaterializedViewRefreshState, data)
