"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceBundleState``."""

from typing import Literal, TypeAlias, cast

WorkspaceBundleState: TypeAlias = Literal[
    "AVAILABLE",
    "PENDING",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceBundleState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkspaceBundleState:
    return cast(WorkspaceBundleState, data)
