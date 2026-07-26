"""Generated from Smithy shape ``com.amazonaws.emr#InstanceRoleType``."""

from typing import Literal, TypeAlias, cast

InstanceRoleType: TypeAlias = Literal[
    "MASTER",
    "CORE",
    "TASK",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceRoleType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceRoleType:
    return cast(InstanceRoleType, data)
