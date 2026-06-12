"""Generated from Smithy shape ``com.amazonaws.connect#CreateAgentStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_status_description
    import aws_sdk_connect.types.agent_status_name
    import aws_sdk_connect.types.agent_status_order_number
    import aws_sdk_connect.types.agent_status_state
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.tag_map


class CreateAgentStatusRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: "aws_sdk_connect.types.agent_status_name.AgentStatusName"
    """<p>The name of the status.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.agent_status_description.AgentStatusDescription"
    ]
    """<p>The description of the status.</p>"""
    state: "aws_sdk_connect.types.agent_status_state.AgentStatusState"
    """<p>The state of the status.</p>"""
    display_order: NotRequired[
        "aws_sdk_connect.types.agent_status_order_number.AgentStatusOrderNumber"
    ]
    """<p>The display order of the status.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentStatusRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_connect.types.agent_status_state

    out["State"] = aws_sdk_connect.types.agent_status_state.serialize_json(
        value["state"]
    )
    if "display_order" in value:
        out["DisplayOrder"] = value["display_order"]
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAgentStatusRequest:
    out: CreateAgentStatusRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateAgentStatusRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "State" in data:
        import aws_sdk_connect.types.agent_status_state

        out["state"] = aws_sdk_connect.types.agent_status_state.deserialize_json(
            data["State"]
        )
    else:
        raise DeserializationError("CreateAgentStatusRequest.state required")
    if "DisplayOrder" in data:
        out["display_order"] = data["DisplayOrder"]
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
