"""Generated from Smithy shape ``com.amazonaws.pcs#SchedulerType``."""

from typing import Literal, TypeAlias, cast

SchedulerType: TypeAlias = Literal["SLURM",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SchedulerType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SchedulerType:
    return cast(SchedulerType, data)
