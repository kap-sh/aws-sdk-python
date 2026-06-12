"""Generated from Smithy shape ``com.amazonaws.codeconnections#RepositorySyncDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeconnections.types.repository_sync_definition

RepositorySyncDefinitionList: TypeAlias = list[
    "aws_sdk_codeconnections.types.repository_sync_definition.RepositorySyncDefinition"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RepositorySyncDefinitionList) -> list:
    import aws_sdk_codeconnections.types.repository_sync_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codeconnections.types.repository_sync_definition.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RepositorySyncDefinitionList:
    import aws_sdk_codeconnections.types.repository_sync_definition

    out: RepositorySyncDefinitionList = []
    for item in data:
        out.append(
            aws_sdk_codeconnections.types.repository_sync_definition.deserialize_aws_json_1_0(
                item
            )
        )
    return out
