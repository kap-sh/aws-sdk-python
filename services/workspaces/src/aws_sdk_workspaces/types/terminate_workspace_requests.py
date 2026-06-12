"""Generated from Smithy shape ``com.amazonaws.workspaces#TerminateWorkspaceRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.terminate_request

TerminateWorkspaceRequests: TypeAlias = list[
    "aws_sdk_workspaces.types.terminate_request.TerminateRequest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminateWorkspaceRequests) -> list:
    import aws_sdk_workspaces.types.terminate_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.terminate_request.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TerminateWorkspaceRequests:
    import aws_sdk_workspaces.types.terminate_request

    out: TerminateWorkspaceRequests = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.terminate_request.deserialize_aws_json_1_1(item)
        )
    return out
