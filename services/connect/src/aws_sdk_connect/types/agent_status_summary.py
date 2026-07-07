"""Generated from Smithy shape ``com.amazonaws.connect#AgentStatusSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_status_id
    import aws_sdk_connect.types.agent_status_name
    import aws_sdk_connect.types.agent_status_type
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.timestamp


class AgentStatusSummary(TypedDict, closed=True):
    id: NotRequired["aws_sdk_connect.types.agent_status_id.AgentStatusId"]
    """<p>The identifier for an agent status.</p>"""
    arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) for the agent status.</p>"""
    name: NotRequired["aws_sdk_connect.types.agent_status_name.AgentStatusName"]
    """<p>The name of the agent status.</p>"""
    type: NotRequired["aws_sdk_connect.types.agent_status_type.AgentStatusType"]
    """<p>The type of the agent status.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentStatusSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import aws_sdk_connect.types.agent_status_type

        out["Type"] = aws_sdk_connect.types.agent_status_type.serialize_json(
            value["type"]
        )
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> AgentStatusSummary:
    out: AgentStatusSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import aws_sdk_connect.types.agent_status_type

        out["type"] = aws_sdk_connect.types.agent_status_type.deserialize_json(
            data["Type"]
        )
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
