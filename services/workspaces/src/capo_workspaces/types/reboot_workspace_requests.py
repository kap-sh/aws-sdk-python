"""Generated from Smithy shape ``com.amazonaws.workspaces#RebootWorkspaceRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.reboot_request

RebootWorkspaceRequests: TypeAlias = list[
    "capo_workspaces.types.reboot_request.RebootRequest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RebootWorkspaceRequests) -> list:
    import capo_workspaces.types.reboot_request

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.reboot_request.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RebootWorkspaceRequests:
    import capo_workspaces.types.reboot_request

    out: RebootWorkspaceRequests = []
    for item in data:
        out.append(capo_workspaces.types.reboot_request.deserialize_aws_json_1_1(item))
    return out
