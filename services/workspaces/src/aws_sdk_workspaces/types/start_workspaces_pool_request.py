"""Generated from Smithy shape ``com.amazonaws.workspaces#StartWorkspacesPoolRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.workspaces_pool_id


class StartWorkspacesPoolRequest(TypedDict, closed=True):
    pool_id: "aws_sdk_workspaces.types.workspaces_pool_id.WorkspacesPoolId"
    """<p>The identifier of the pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartWorkspacesPoolRequest) -> dict:
    out: dict = {}
    out["PoolId"] = value["pool_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartWorkspacesPoolRequest:
    out: StartWorkspacesPoolRequest = {}  # type: ignore[typeddict-item]
    if "PoolId" in data:
        out["pool_id"] = data["PoolId"]
    else:
        raise DeserializationError("StartWorkspacesPoolRequest.pool_id required")
    return out
