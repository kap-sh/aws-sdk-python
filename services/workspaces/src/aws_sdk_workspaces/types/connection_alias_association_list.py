"""Generated from Smithy shape ``com.amazonaws.workspaces#ConnectionAliasAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.connection_alias_association

ConnectionAliasAssociationList: TypeAlias = list[
    "aws_sdk_workspaces.types.connection_alias_association.ConnectionAliasAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionAliasAssociationList) -> list:
    import aws_sdk_workspaces.types.connection_alias_association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.connection_alias_association.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectionAliasAssociationList:
    import aws_sdk_workspaces.types.connection_alias_association

    out: ConnectionAliasAssociationList = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.connection_alias_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out
