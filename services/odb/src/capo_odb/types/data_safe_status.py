"""Generated from Smithy shape ``com.amazonaws.odb#DataSafeStatus``."""

from typing import Literal, TypeAlias, cast

DataSafeStatus: TypeAlias = Literal[
    "REGISTERING",
    "REGISTERED",
    "DEREGISTERING",
    "NOT_REGISTERED",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataSafeStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DataSafeStatus:
    return cast(DataSafeStatus, data)
