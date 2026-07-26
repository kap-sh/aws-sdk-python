"""Generated from Smithy shape ``com.amazonaws.workspaces#ApplicationResourceAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.application_resource_association

ApplicationResourceAssociationList: TypeAlias = list[
    "capo_workspaces.types.application_resource_association.ApplicationResourceAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationResourceAssociationList) -> list:
    import capo_workspaces.types.application_resource_association

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.application_resource_association.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ApplicationResourceAssociationList:
    import capo_workspaces.types.application_resource_association

    out: ApplicationResourceAssociationList = []
    for item in data:
        out.append(
            capo_workspaces.types.application_resource_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out
