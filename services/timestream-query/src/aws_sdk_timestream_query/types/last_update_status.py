"""Generated from Smithy shape ``com.amazonaws.timestreamquery#LastUpdateStatus``."""

from typing import Literal, TypeAlias, cast

LastUpdateStatus: TypeAlias = Literal[
    "PENDING",
    "FAILED",
    "SUCCEEDED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LastUpdateStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LastUpdateStatus:
    return cast(LastUpdateStatus, data)
