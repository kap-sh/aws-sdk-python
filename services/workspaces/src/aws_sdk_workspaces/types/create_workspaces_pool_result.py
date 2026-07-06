"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateWorkspacesPoolResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.workspaces_pool


class CreateWorkspacesPoolResult(TypedDict, closed=True):
    workspaces_pool: NotRequired[
        "aws_sdk_workspaces.types.workspaces_pool.WorkspacesPool"
    ]
    """<p>Indicates the pool to create.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWorkspacesPoolResult) -> dict:
    out: dict = {}
    if "workspaces_pool" in value:
        import aws_sdk_workspaces.types.workspaces_pool

        out["WorkspacesPool"] = (
            aws_sdk_workspaces.types.workspaces_pool.serialize_aws_json_1_1(
                value["workspaces_pool"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWorkspacesPoolResult:
    out: CreateWorkspacesPoolResult = {}  # type: ignore[typeddict-item]
    if "WorkspacesPool" in data:
        import aws_sdk_workspaces.types.workspaces_pool

        out["workspaces_pool"] = (
            aws_sdk_workspaces.types.workspaces_pool.deserialize_aws_json_1_1(
                data["WorkspacesPool"]
            )
        )
    return out
