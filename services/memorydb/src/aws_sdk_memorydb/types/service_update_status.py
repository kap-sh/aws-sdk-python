"""Generated from Smithy shape ``com.amazonaws.memorydb#ServiceUpdateStatus``."""

from typing import Literal, TypeAlias, cast

ServiceUpdateStatus: TypeAlias = Literal[
    "available",
    "in-progress",
    "complete",
    "scheduled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceUpdateStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceUpdateStatus:
    return cast(ServiceUpdateStatus, data)
