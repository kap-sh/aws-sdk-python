"""Generated from Smithy shape ``com.amazonaws.workspaces#StartWorkspaceRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.start_request

StartWorkspaceRequests: TypeAlias = list[
    "capo_workspaces.types.start_request.StartRequest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartWorkspaceRequests) -> list:
    import capo_workspaces.types.start_request

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.start_request.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StartWorkspaceRequests:
    import capo_workspaces.types.start_request

    out: StartWorkspaceRequests = []
    for item in data:
        out.append(capo_workspaces.types.start_request.deserialize_aws_json_1_1(item))
    return out
