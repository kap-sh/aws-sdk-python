"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#AgentConfigurationStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.agent_configuration_status

AgentConfigurationStatusList: TypeAlias = list[
    "aws_sdk_application_discovery_service.types.agent_configuration_status.AgentConfigurationStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentConfigurationStatusList) -> list:
    import aws_sdk_application_discovery_service.types.agent_configuration_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_discovery_service.types.agent_configuration_status.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AgentConfigurationStatusList:
    import aws_sdk_application_discovery_service.types.agent_configuration_status

    out: AgentConfigurationStatusList = []
    for item in data:
        out.append(
            aws_sdk_application_discovery_service.types.agent_configuration_status.deserialize_aws_json_1_1(
                item
            )
        )
    return out
