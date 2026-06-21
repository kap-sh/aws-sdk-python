"""Generated from Smithy shape ``com.amazonaws.athena#WorkGroupState``."""

from typing import Literal, TypeAlias, cast

WorkGroupState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkGroupState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkGroupState:
    return cast(WorkGroupState, data)
