"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#StopDataCollectionByAgentIdsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.agent_configuration_status_list


class StopDataCollectionByAgentIdsResponse(TypedDict, closed=True):
    agents_configuration_status: NotRequired[
        "aws_sdk_application_discovery_service.types.agent_configuration_status_list.AgentConfigurationStatusList"
    ]
    """<p>Information about the agents that were instructed to stop collecting data. Information includes the agent ID, a description of the operation performed, and whether the agent configuration was updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopDataCollectionByAgentIdsResponse) -> dict:
    out: dict = {}
    if "agents_configuration_status" in value:
        import aws_sdk_application_discovery_service.types.agent_configuration_status_list

        out["agentsConfigurationStatus"] = (
            aws_sdk_application_discovery_service.types.agent_configuration_status_list.serialize_aws_json_1_1(
                value["agents_configuration_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopDataCollectionByAgentIdsResponse:
    out: StopDataCollectionByAgentIdsResponse = {}  # type: ignore[typeddict-item]
    if "agentsConfigurationStatus" in data:
        import aws_sdk_application_discovery_service.types.agent_configuration_status_list

        out["agents_configuration_status"] = (
            aws_sdk_application_discovery_service.types.agent_configuration_status_list.deserialize_aws_json_1_1(
                data["agentsConfigurationStatus"]
            )
        )
    return out
