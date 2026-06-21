"""Generated from Smithy shape ``com.amazonaws.emr#InstanceGroupType``."""

from typing import Literal, TypeAlias, cast

InstanceGroupType: TypeAlias = Literal[
    "MASTER",
    "CORE",
    "TASK",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceGroupType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceGroupType:
    return cast(InstanceGroupType, data)
