"""Generated from Smithy shape ``com.amazonaws.workspaces#ConnectionAliasList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.connection_alias

ConnectionAliasList: TypeAlias = list[
    "capo_workspaces.types.connection_alias.ConnectionAlias"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionAliasList) -> list:
    import capo_workspaces.types.connection_alias

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.connection_alias.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectionAliasList:
    import capo_workspaces.types.connection_alias

    out: ConnectionAliasList = []
    for item in data:
        out.append(
            capo_workspaces.types.connection_alias.deserialize_aws_json_1_1(item)
        )
    return out
