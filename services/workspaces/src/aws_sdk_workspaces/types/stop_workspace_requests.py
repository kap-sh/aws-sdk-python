"""Generated from Smithy shape ``com.amazonaws.workspaces#StopWorkspaceRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.stop_request

StopWorkspaceRequests: TypeAlias = list[
    "aws_sdk_workspaces.types.stop_request.StopRequest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopWorkspaceRequests) -> list:
    import aws_sdk_workspaces.types.stop_request

    out: list = []
    for item in value:
        out.append(aws_sdk_workspaces.types.stop_request.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StopWorkspaceRequests:
    import aws_sdk_workspaces.types.stop_request

    out: StopWorkspaceRequests = []
    for item in data:
        out.append(aws_sdk_workspaces.types.stop_request.deserialize_aws_json_1_1(item))
    return out
