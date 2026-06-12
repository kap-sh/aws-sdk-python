"""Generated from Smithy shape ``com.amazonaws.workspaces#ApplicationResourceAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.application_resource_association

ApplicationResourceAssociationList: TypeAlias = list[
    "aws_sdk_workspaces.types.application_resource_association.ApplicationResourceAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationResourceAssociationList) -> list:
    import aws_sdk_workspaces.types.application_resource_association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.application_resource_association.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ApplicationResourceAssociationList:
    import aws_sdk_workspaces.types.application_resource_association

    out: ApplicationResourceAssociationList = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.application_resource_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out
