"""Generated from Smithy shape ``com.amazonaws.datasync#DescribeAgentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datasync.types.agent_arn
    import aws_sdk_datasync.types.agent_status
    import aws_sdk_datasync.types.endpoint_type
    import aws_sdk_datasync.types.platform
    import aws_sdk_datasync.types.private_link_config
    import aws_sdk_datasync.types.tag_value
    import aws_sdk_datasync.types.time


class DescribeAgentResponse(TypedDict):
    agent_arn: NotRequired["aws_sdk_datasync.types.agent_arn.AgentArn"]
    """<p>The ARN of the agent.</p>"""
    name: NotRequired["aws_sdk_datasync.types.tag_value.TagValue"]
    """<p>The name of the agent.</p>"""
    status: NotRequired["aws_sdk_datasync.types.agent_status.AgentStatus"]
    """<p>The status of the agent.</p> <ul> <li> <p>If the status is <code>ONLINE</code>, the agent is configured properly and ready to use.</p> </li> <li> <p>If the status is <code>OFFLINE</code>, the agent has been out of contact with DataSync for five minutes or longer. This can happen for a few reasons. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-datasync-agents.html#troubleshoot-agent-offline\">What do I do if my agent is offline?</a> </p> </li> </ul>"""
    last_connection_time: NotRequired["aws_sdk_datasync.types.time.Time"]
    """<p>The last time that the agent was communicating with the DataSync service.</p>"""
    creation_time: NotRequired["aws_sdk_datasync.types.time.Time"]
    """<p>The time that the agent was <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/activate-agent.html\">activated</a>.</p>"""
    endpoint_type: NotRequired["aws_sdk_datasync.types.endpoint_type.EndpointType"]
    """<p>The type of <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/choose-service-endpoint.html\">service endpoint</a> that your agent is connected to.</p>"""
    private_link_config: NotRequired[
        "aws_sdk_datasync.types.private_link_config.PrivateLinkConfig"
    ]
    """<p>The network configuration that the agent uses when connecting to a <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/choose-service-endpoint.html#choose-service-endpoint-vpc\">VPC service endpoint</a>.</p>"""
    platform: NotRequired["aws_sdk_datasync.types.platform.Platform"]
    """<p>The platform-related details about the agent, such as the version number.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAgentResponse) -> dict:
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
    if "last_connection_time" in value:
        import aws_sdk_datasync.types.time

        out["LastConnectionTime"] = aws_sdk_datasync.types.time.serialize_aws_json_1_1(
            value["last_connection_time"]
        )
    if "creation_time" in value:
        import aws_sdk_datasync.types.time

        out["CreationTime"] = aws_sdk_datasync.types.time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "endpoint_type" in value:
        import aws_sdk_datasync.types.endpoint_type

        out["EndpointType"] = (
            aws_sdk_datasync.types.endpoint_type.serialize_aws_json_1_1(
                value["endpoint_type"]
            )
        )
    if "private_link_config" in value:
        import aws_sdk_datasync.types.private_link_config

        out["PrivateLinkConfig"] = (
            aws_sdk_datasync.types.private_link_config.serialize_aws_json_1_1(
                value["private_link_config"]
            )
        )
    if "platform" in value:
        import aws_sdk_datasync.types.platform

        out["Platform"] = aws_sdk_datasync.types.platform.serialize_aws_json_1_1(
            value["platform"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAgentResponse:
    out: DescribeAgentResponse = {}  # type: ignore[typeddict-item]
    if "AgentArn" in data:
        out["agent_arn"] = data["AgentArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import aws_sdk_datasync.types.agent_status

        out["status"] = aws_sdk_datasync.types.agent_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "LastConnectionTime" in data:
        import aws_sdk_datasync.types.time

        out["last_connection_time"] = (
            aws_sdk_datasync.types.time.deserialize_aws_json_1_1(
                data["LastConnectionTime"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_datasync.types.time

        out["creation_time"] = aws_sdk_datasync.types.time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "EndpointType" in data:
        import aws_sdk_datasync.types.endpoint_type

        out["endpoint_type"] = (
            aws_sdk_datasync.types.endpoint_type.deserialize_aws_json_1_1(
                data["EndpointType"]
            )
        )
    if "PrivateLinkConfig" in data:
        import aws_sdk_datasync.types.private_link_config

        out["private_link_config"] = (
            aws_sdk_datasync.types.private_link_config.deserialize_aws_json_1_1(
                data["PrivateLinkConfig"]
            )
        )
    if "Platform" in data:
        import aws_sdk_datasync.types.platform

        out["platform"] = aws_sdk_datasync.types.platform.deserialize_aws_json_1_1(
            data["Platform"]
        )
    return out
