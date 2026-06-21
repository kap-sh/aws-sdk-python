"""Generated from Smithy shape ``com.amazonaws.workspaces#OperatingSystemType``."""

from typing import Literal, TypeAlias, cast

OperatingSystemType: TypeAlias = Literal[
    "WINDOWS",
    "LINUX",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperatingSystemType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OperatingSystemType:
    return cast(OperatingSystemType, data)
