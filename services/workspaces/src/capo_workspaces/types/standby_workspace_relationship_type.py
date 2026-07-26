"""Generated from Smithy shape ``com.amazonaws.workspaces#StandbyWorkspaceRelationshipType``."""

from typing import Literal, TypeAlias, cast

StandbyWorkspaceRelationshipType: TypeAlias = Literal[
    "PRIMARY",
    "STANDBY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StandbyWorkspaceRelationshipType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StandbyWorkspaceRelationshipType:
    return cast(StandbyWorkspaceRelationshipType, data)
