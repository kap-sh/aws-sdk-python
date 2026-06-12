"""Generated from Smithy shape ``com.amazonaws.workspaces#ConnectionAliasIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.connection_alias_id

ConnectionAliasIdList: TypeAlias = list[
    "aws_sdk_workspaces.types.connection_alias_id.ConnectionAliasId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionAliasIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ConnectionAliasIdList:
    return list(data)
