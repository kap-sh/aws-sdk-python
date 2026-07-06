"""Generated from Smithy shape ``com.amazonaws.workspaces#StopWorkspacesPoolRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.workspaces_pool_id


class StopWorkspacesPoolRequest(TypedDict, closed=True):
    pool_id: "aws_sdk_workspaces.types.workspaces_pool_id.WorkspacesPoolId"
    """<p>The identifier of the pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopWorkspacesPoolRequest) -> dict:
    out: dict = {}
    out["PoolId"] = value["pool_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopWorkspacesPoolRequest:
    out: StopWorkspacesPoolRequest = {}  # type: ignore[typeddict-item]
    if "PoolId" in data:
        out["pool_id"] = data["PoolId"]
    else:
        raise DeserializationError("StopWorkspacesPoolRequest.pool_id required")
    return out
