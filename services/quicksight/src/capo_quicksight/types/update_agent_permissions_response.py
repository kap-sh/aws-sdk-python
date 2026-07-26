"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateAgentPermissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.agent_arn
    import capo_quicksight.types.agent_id
    import capo_quicksight.types.resource_permission_list


class UpdateAgentPermissionsResponse(TypedDict, closed=True):
    arn: "capo_quicksight.types.agent_arn.AgentArn"
    """<p>The Amazon Resource Name (ARN) of the agent.</p>"""
    agent_id: "capo_quicksight.types.agent_id.AgentId"
    """<p>The unique identifier for the agent.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    permissions: NotRequired[
        "capo_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>The resource permissions for the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentPermissionsResponse) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["AgentId"] = value["agent_id"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "permissions" in value:
        import capo_quicksight.types.resource_permission_list

        out["Permissions"] = (
            capo_quicksight.types.resource_permission_list.serialize_json(
                value["permissions"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAgentPermissionsResponse:
    out: UpdateAgentPermissionsResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("UpdateAgentPermissionsResponse.arn required")
    if "AgentId" in data:
        out["agent_id"] = data["AgentId"]
    else:
        raise DeserializationError("UpdateAgentPermissionsResponse.agent_id required")
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "Permissions" in data:
        import capo_quicksight.types.resource_permission_list

        out["permissions"] = (
            capo_quicksight.types.resource_permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    return out
