"""Generated from Smithy shape ``com.amazonaws.emr#InstanceFleetType``."""

from typing import Literal, TypeAlias, cast

InstanceFleetType: TypeAlias = Literal[
    "MASTER",
    "CORE",
    "TASK",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceFleetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceFleetType:
    return cast(InstanceFleetType, data)
