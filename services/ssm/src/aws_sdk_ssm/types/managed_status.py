"""Generated from Smithy shape ``com.amazonaws.ssm#ManagedStatus``."""

from typing import Literal, TypeAlias, cast

ManagedStatus: TypeAlias = Literal[
    "All",
    "Managed",
    "Unmanaged",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManagedStatus:
    return cast(ManagedStatus, data)
