"""Generated from Smithy shape ``com.amazonaws.ecs#CPUArchitecture``."""

from typing import Literal, TypeAlias, cast

CPUArchitecture: TypeAlias = Literal[
    "X86_64",
    "ARM64",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CPUArchitecture) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CPUArchitecture:
    return cast(CPUArchitecture, data)
