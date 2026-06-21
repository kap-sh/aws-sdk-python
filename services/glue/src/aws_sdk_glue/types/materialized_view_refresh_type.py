"""Generated from Smithy shape ``com.amazonaws.glue#MaterializedViewRefreshType``."""

from typing import Literal, TypeAlias, cast

MaterializedViewRefreshType: TypeAlias = Literal[
    "FULL",
    "INCREMENTAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaterializedViewRefreshType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MaterializedViewRefreshType:
    return cast(MaterializedViewRefreshType, data)
