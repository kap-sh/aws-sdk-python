"""Generated from Smithy shape ``com.amazonaws.evs#VlanState``."""

from typing import Literal, TypeAlias, cast

VlanState: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "DELETING",
    "DELETED",
    "CREATE_FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VlanState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> VlanState:
    return cast(VlanState, data)
