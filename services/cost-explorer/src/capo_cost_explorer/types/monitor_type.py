"""Generated from Smithy shape ``com.amazonaws.costexplorer#MonitorType``."""

from typing import Literal, TypeAlias, cast

MonitorType: TypeAlias = Literal[
    "DIMENSIONAL",
    "CUSTOM",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MonitorType:
    return cast(MonitorType, data)
