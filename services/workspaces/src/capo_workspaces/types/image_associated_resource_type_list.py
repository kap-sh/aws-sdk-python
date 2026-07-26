"""Generated from Smithy shape ``com.amazonaws.workspaces#ImageAssociatedResourceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.image_associated_resource_type

ImageAssociatedResourceTypeList: TypeAlias = list[
    "capo_workspaces.types.image_associated_resource_type.ImageAssociatedResourceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageAssociatedResourceTypeList) -> list:
    import capo_workspaces.types.image_associated_resource_type

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.image_associated_resource_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ImageAssociatedResourceTypeList:
    import capo_workspaces.types.image_associated_resource_type

    out: ImageAssociatedResourceTypeList = []
    for item in data:
        out.append(
            capo_workspaces.types.image_associated_resource_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
