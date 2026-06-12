"""Generated from Smithy shape ``com.amazonaws.workspaces#ImageResourceAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.image_resource_association

ImageResourceAssociationList: TypeAlias = list[
    "aws_sdk_workspaces.types.image_resource_association.ImageResourceAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageResourceAssociationList) -> list:
    import aws_sdk_workspaces.types.image_resource_association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.image_resource_association.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ImageResourceAssociationList:
    import aws_sdk_workspaces.types.image_resource_association

    out: ImageResourceAssociationList = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.image_resource_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out
