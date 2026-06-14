"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateWorkspacesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.workspace_request_list


class CreateWorkspacesRequest(TypedDict):
    workspaces: "aws_sdk_workspaces.types.workspace_request_list.WorkspaceRequestList"
    """<p>The WorkSpaces to create. You can specify up to 25 WorkSpaces.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWorkspacesRequest) -> dict:
    out: dict = {}
    import aws_sdk_workspaces.types.workspace_request_list

    out["Workspaces"] = (
        aws_sdk_workspaces.types.workspace_request_list.serialize_aws_json_1_1(
            value["workspaces"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWorkspacesRequest:
    out: CreateWorkspacesRequest = {}  # type: ignore[typeddict-item]
    if "Workspaces" in data:
        import aws_sdk_workspaces.types.workspace_request_list

        out["workspaces"] = (
            aws_sdk_workspaces.types.workspace_request_list.deserialize_aws_json_1_1(
                data["Workspaces"]
            )
        )
    else:
        raise DeserializationError("CreateWorkspacesRequest.workspaces required")
    return out
