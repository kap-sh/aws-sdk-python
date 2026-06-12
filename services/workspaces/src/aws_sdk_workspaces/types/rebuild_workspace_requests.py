"""Generated from Smithy shape ``com.amazonaws.workspaces#RebuildWorkspaceRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.rebuild_request

RebuildWorkspaceRequests: TypeAlias = list[
    "aws_sdk_workspaces.types.rebuild_request.RebuildRequest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RebuildWorkspaceRequests) -> list:
    import aws_sdk_workspaces.types.rebuild_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.rebuild_request.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RebuildWorkspaceRequests:
    import aws_sdk_workspaces.types.rebuild_request

    out: RebuildWorkspaceRequests = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.rebuild_request.deserialize_aws_json_1_1(item)
        )
    return out
