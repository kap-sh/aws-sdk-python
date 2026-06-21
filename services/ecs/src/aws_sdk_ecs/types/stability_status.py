"""Generated from Smithy shape ``com.amazonaws.ecs#StabilityStatus``."""

from typing import Literal, TypeAlias, cast

StabilityStatus: TypeAlias = Literal[
    "STEADY_STATE",
    "STABILIZING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StabilityStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StabilityStatus:
    return cast(StabilityStatus, data)
