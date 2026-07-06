"""Generated from Smithy shape ``com.amazonaws.connect#AgentStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_status_description
    import aws_sdk_connect.types.agent_status_id
    import aws_sdk_connect.types.agent_status_name
    import aws_sdk_connect.types.agent_status_order_number
    import aws_sdk_connect.types.agent_status_state
    import aws_sdk_connect.types.agent_status_type
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.timestamp


class AgentStatus(TypedDict, closed=True):
    agent_status_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the agent status.</p>"""
    agent_status_id: NotRequired["aws_sdk_connect.types.agent_status_id.AgentStatusId"]
    """<p>The identifier of the agent status.</p>"""
    name: NotRequired["aws_sdk_connect.types.agent_status_name.AgentStatusName"]
    """<p>The name of the agent status.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.agent_status_description.AgentStatusDescription"
    ]
    """<p>The description of the agent status.</p>"""
    type: NotRequired["aws_sdk_connect.types.agent_status_type.AgentStatusType"]
    """<p>The type of agent status.</p>"""
    display_order: NotRequired[
        "aws_sdk_connect.types.agent_status_order_number.AgentStatusOrderNumber"
    ]
    """<p>The display order of the agent status.</p>"""
    state: NotRequired["aws_sdk_connect.types.agent_status_state.AgentStatusState"]
    """<p>The state of the agent status.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    r"""<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentStatus) -> dict:
    out: dict = {}
    if "agent_status_arn" in value:
        out["AgentStatusARN"] = value["agent_status_arn"]
    if "agent_status_id" in value:
        out["AgentStatusId"] = value["agent_status_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        import aws_sdk_connect.types.agent_status_type

        out["Type"] = aws_sdk_connect.types.agent_status_type.serialize_json(
            value["type"]
        )
    if "display_order" in value:
        out["DisplayOrder"] = value["display_order"]
    if "state" in value:
        import aws_sdk_connect.types.agent_status_state

        out["State"] = aws_sdk_connect.types.agent_status_state.serialize_json(
            value["state"]
        )
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> AgentStatus:
    out: AgentStatus = {}  # type: ignore[typeddict-item]
    if "AgentStatusARN" in data:
        out["agent_status_arn"] = data["AgentStatusARN"]
    if "AgentStatusId" in data:
        out["agent_status_id"] = data["AgentStatusId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Type" in data:
        import aws_sdk_connect.types.agent_status_type

        out["type"] = aws_sdk_connect.types.agent_status_type.deserialize_json(
            data["Type"]
        )
    if "DisplayOrder" in data:
        out["display_order"] = data["DisplayOrder"]
    if "State" in data:
        import aws_sdk_connect.types.agent_status_state

        out["state"] = aws_sdk_connect.types.agent_status_state.deserialize_json(
            data["State"]
        )
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
