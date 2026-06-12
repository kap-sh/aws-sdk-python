"""Generated from Smithy shape ``com.amazonaws.connect#UpdateAgentStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_status_id
    import aws_sdk_connect.types.agent_status_name
    import aws_sdk_connect.types.agent_status_order_number
    import aws_sdk_connect.types.agent_status_state
    import aws_sdk_connect.types.boolean
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.update_agent_status_description


class UpdateAgentStatusRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    agent_status_id: "aws_sdk_connect.types.agent_status_id.AgentStatusId"
    """<p>The identifier of the agent status.</p>"""
    name: NotRequired["aws_sdk_connect.types.agent_status_name.AgentStatusName"]
    """<p>The name of the agent status.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.update_agent_status_description.UpdateAgentStatusDescription"
    ]
    """<p>The description of the agent status.</p>"""
    state: NotRequired["aws_sdk_connect.types.agent_status_state.AgentStatusState"]
    """<p>The state of the agent status.</p>"""
    display_order: NotRequired[
        "aws_sdk_connect.types.agent_status_order_number.AgentStatusOrderNumber"
    ]
    """<p>The display order of the agent status.</p>"""
    reset_order_number: "aws_sdk_connect.types.boolean.Boolean"
    """<p>A number indicating the reset order of the agent status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentStatusRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "state" in value:
        import aws_sdk_connect.types.agent_status_state

        out["State"] = aws_sdk_connect.types.agent_status_state.serialize_json(
            value["state"]
        )
    if "display_order" in value:
        out["DisplayOrder"] = value["display_order"]
    out["ResetOrderNumber"] = value.get("reset_order_number", False)
    return out


def deserialize_json(data: dict) -> UpdateAgentStatusRequest:
    out: UpdateAgentStatusRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "State" in data:
        import aws_sdk_connect.types.agent_status_state

        out["state"] = aws_sdk_connect.types.agent_status_state.deserialize_json(
            data["State"]
        )
    if "DisplayOrder" in data:
        out["display_order"] = data["DisplayOrder"]
    if "ResetOrderNumber" in data:
        out["reset_order_number"] = data["ResetOrderNumber"]
    else:
        out["reset_order_number"] = False
    return out
