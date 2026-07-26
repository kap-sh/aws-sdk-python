"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceImageRequiredTenancy``."""

from typing import Literal, TypeAlias, cast

WorkspaceImageRequiredTenancy: TypeAlias = Literal[
    "DEFAULT",
    "DEDICATED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceImageRequiredTenancy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkspaceImageRequiredTenancy:
    return cast(WorkspaceImageRequiredTenancy, data)
