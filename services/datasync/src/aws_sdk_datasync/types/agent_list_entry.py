"""Generated from Smithy shape ``com.amazonaws.datasync#AgentListEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datasync.types.agent_arn
    import aws_sdk_datasync.types.agent_status
    import aws_sdk_datasync.types.platform
    import aws_sdk_datasync.types.tag_value


class AgentListEntry(TypedDict, closed=True):
    agent_arn: NotRequired["aws_sdk_datasync.types.agent_arn.AgentArn"]
    """<p>The Amazon Resource Name (ARN) of a DataSync agent.</p>"""
    name: NotRequired["aws_sdk_datasync.types.tag_value.TagValue"]
    """<p>The name of an agent.</p>"""
    status: NotRequired["aws_sdk_datasync.types.agent_status.AgentStatus"]
    r"""<p>The status of an agent.</p> <ul> <li> <p>If the status is <code>ONLINE</code>, the agent is configured properly and ready to use.</p> </li> <li> <p>If the status is <code>OFFLINE</code>, the agent has been out of contact with DataSync for five minutes or longer. This can happen for a few reasons. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-datasync-agents.html#troubleshoot-agent-offline\">What do I do if my agent is offline?</a> </p> </li> </ul>"""
    platform: NotRequired["aws_sdk_datasync.types.platform.Platform"]
    """<p>The platform-related details about the agent, such as the version number.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentListEntry) -> dict:
    out: dict = {}
    if "agent_arn" in value:
        out["AgentArn"] = value["agent_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_datasync.types.agent_status

        out["Status"] = aws_sdk_datasync.types.agent_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "platform" in value:
        import aws_sdk_datasync.types.platform

        out["Platform"] = aws_sdk_datasync.types.platform.serialize_aws_json_1_1(
            value["platform"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AgentListEntry:
    out: AgentListEntry = {}  # type: ignore[typeddict-item]
    if "AgentArn" in data:
        out["agent_arn"] = data["AgentArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import aws_sdk_datasync.types.agent_status

        out["status"] = aws_sdk_datasync.types.agent_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "Platform" in data:
        import aws_sdk_datasync.types.platform

        out["platform"] = aws_sdk_datasync.types.platform.deserialize_aws_json_1_1(
            data["Platform"]
        )
    return out
