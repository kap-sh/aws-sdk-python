"""Generated from Smithy shape ``com.amazonaws.costexplorer#MonitorDimension``."""

from typing import Literal, TypeAlias, cast

MonitorDimension: TypeAlias = Literal[
    "SERVICE",
    "LINKED_ACCOUNT",
    "TAG",
    "COST_CATEGORY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitorDimension) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MonitorDimension:
    return cast(MonitorDimension, data)
