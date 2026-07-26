"""Generated from Smithy shape ``com.amazonaws.glue#LastRefreshType``."""

from typing import Literal, TypeAlias, cast

LastRefreshType: TypeAlias = Literal[
    "FULL",
    "INCREMENTAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LastRefreshType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LastRefreshType:
    return cast(LastRefreshType, data)
