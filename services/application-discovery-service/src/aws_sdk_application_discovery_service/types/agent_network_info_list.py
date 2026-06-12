"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#AgentNetworkInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.agent_network_info

AgentNetworkInfoList: TypeAlias = list[
    "aws_sdk_application_discovery_service.types.agent_network_info.AgentNetworkInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentNetworkInfoList) -> list:
    import aws_sdk_application_discovery_service.types.agent_network_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_discovery_service.types.agent_network_info.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AgentNetworkInfoList:
    import aws_sdk_application_discovery_service.types.agent_network_info

    out: AgentNetworkInfoList = []
    for item in data:
        out.append(
            aws_sdk_application_discovery_service.types.agent_network_info.deserialize_aws_json_1_1(
                item
            )
        )
    return out
