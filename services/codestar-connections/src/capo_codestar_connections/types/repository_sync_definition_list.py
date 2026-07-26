"""Generated from Smithy shape ``com.amazonaws.codestarconnections#RepositorySyncDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codestar_connections.types.repository_sync_definition

RepositorySyncDefinitionList: TypeAlias = list[
    "capo_codestar_connections.types.repository_sync_definition.RepositorySyncDefinition"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RepositorySyncDefinitionList) -> list:
    import capo_codestar_connections.types.repository_sync_definition

    out: list = []
    for item in value:
        out.append(
            capo_codestar_connections.types.repository_sync_definition.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RepositorySyncDefinitionList:
    import capo_codestar_connections.types.repository_sync_definition

    out: RepositorySyncDefinitionList = []
    for item in data:
        out.append(
            capo_codestar_connections.types.repository_sync_definition.deserialize_aws_json_1_0(
                item
            )
        )
    return out
