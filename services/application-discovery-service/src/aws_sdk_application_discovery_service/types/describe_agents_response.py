"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DescribeAgentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.agents_info
    import aws_sdk_application_discovery_service.types.next_token


class DescribeAgentsResponse(TypedDict, closed=True):
    agents_info: NotRequired[
        "aws_sdk_application_discovery_service.types.agents_info.AgentsInfo"
    ]
    """<p>Lists agents or the collector by ID or lists all agents/collectors associated with your user, if you did not specify an agent/collector ID. The output includes agent/collector IDs, IP addresses, media access control (MAC) addresses, agent/collector health, host name where the agent/collector resides, and the version number of each agent/collector.</p>"""
    next_token: NotRequired[
        "aws_sdk_application_discovery_service.types.next_token.NextToken"
    ]
    """<p>Token to retrieve the next set of results. For example, if you specified 100 IDs for <code>DescribeAgentsRequest$agentIds</code> but set <code>DescribeAgentsRequest$maxResults</code> to 10, you received a set of 10 results along with this token. Use this token in the next query to retrieve the next set of 10.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAgentsResponse) -> dict:
    out: dict = {}
    if "agents_info" in value:
        import aws_sdk_application_discovery_service.types.agents_info

        out["agentsInfo"] = (
            aws_sdk_application_discovery_service.types.agents_info.serialize_aws_json_1_1(
                value["agents_info"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAgentsResponse:
    out: DescribeAgentsResponse = {}  # type: ignore[typeddict-item]
    if "agentsInfo" in data:
        import aws_sdk_application_discovery_service.types.agents_info

        out["agents_info"] = (
            aws_sdk_application_discovery_service.types.agents_info.deserialize_aws_json_1_1(
                data["agentsInfo"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
