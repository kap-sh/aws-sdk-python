"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeAgentPermissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.agent_arn
    import aws_sdk_quicksight.types.agent_id
    import aws_sdk_quicksight.types.resource_permission_list


class DescribeAgentPermissionsResponse(TypedDict, closed=True):
    arn: "aws_sdk_quicksight.types.agent_arn.AgentArn"
    """<p>The Amazon Resource Name (ARN) of the agent.</p>"""
    agent_id: "aws_sdk_quicksight.types.agent_id.AgentId"
    """<p>The unique identifier for the agent.</p>"""
    permissions: (
        "aws_sdk_quicksight.types.resource_permission_list.ResourcePermissionList"
    )
    """<p>The resource permissions for the agent.</p>"""
    request_id: "str"
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAgentPermissionsResponse) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["AgentId"] = value["agent_id"]
    import aws_sdk_quicksight.types.resource_permission_list

    out["Permissions"] = (
        aws_sdk_quicksight.types.resource_permission_list.serialize_json(
            value["permissions"]
        )
    )
    out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeAgentPermissionsResponse:
    out: DescribeAgentPermissionsResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DescribeAgentPermissionsResponse.arn required")
    if "AgentId" in data:
        out["agent_id"] = data["AgentId"]
    else:
        raise DeserializationError("DescribeAgentPermissionsResponse.agent_id required")
    if "Permissions" in data:
        import aws_sdk_quicksight.types.resource_permission_list

        out["permissions"] = (
            aws_sdk_quicksight.types.resource_permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAgentPermissionsResponse.permissions required"
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    else:
        raise DeserializationError(
            "DescribeAgentPermissionsResponse.request_id required"
        )
    return out
