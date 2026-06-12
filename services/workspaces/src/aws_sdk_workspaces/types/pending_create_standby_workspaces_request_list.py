"""Generated from Smithy shape ``com.amazonaws.workspaces#PendingCreateStandbyWorkspacesRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.pending_create_standby_workspaces_request

PendingCreateStandbyWorkspacesRequestList: TypeAlias = list[
    "aws_sdk_workspaces.types.pending_create_standby_workspaces_request.PendingCreateStandbyWorkspacesRequest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PendingCreateStandbyWorkspacesRequestList) -> list:
    import aws_sdk_workspaces.types.pending_create_standby_workspaces_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.pending_create_standby_workspaces_request.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PendingCreateStandbyWorkspacesRequestList:
    import aws_sdk_workspaces.types.pending_create_standby_workspaces_request

    out: PendingCreateStandbyWorkspacesRequestList = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.pending_create_standby_workspaces_request.deserialize_aws_json_1_1(
                item
            )
        )
    return out
