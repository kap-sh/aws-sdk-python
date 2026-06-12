"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkSpaceApplicationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.work_space_application

WorkSpaceApplicationList: TypeAlias = list[
    "aws_sdk_workspaces.types.work_space_application.WorkSpaceApplication"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkSpaceApplicationList) -> list:
    import aws_sdk_workspaces.types.work_space_application

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.work_space_application.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> WorkSpaceApplicationList:
    import aws_sdk_workspaces.types.work_space_application

    out: WorkSpaceApplicationList = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.work_space_application.deserialize_aws_json_1_1(
                item
            )
        )
    return out
