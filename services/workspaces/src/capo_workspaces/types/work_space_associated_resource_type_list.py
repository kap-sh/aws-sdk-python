"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkSpaceAssociatedResourceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.work_space_associated_resource_type

WorkSpaceAssociatedResourceTypeList: TypeAlias = list[
    "capo_workspaces.types.work_space_associated_resource_type.WorkSpaceAssociatedResourceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkSpaceAssociatedResourceTypeList) -> list:
    import capo_workspaces.types.work_space_associated_resource_type

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.work_space_associated_resource_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> WorkSpaceAssociatedResourceTypeList:
    import capo_workspaces.types.work_space_associated_resource_type

    out: WorkSpaceAssociatedResourceTypeList = []
    for item in data:
        out.append(
            capo_workspaces.types.work_space_associated_resource_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
