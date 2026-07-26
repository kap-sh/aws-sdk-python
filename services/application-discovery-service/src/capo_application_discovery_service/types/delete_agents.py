"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DeleteAgents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_discovery_service.types.delete_agent

DeleteAgents: TypeAlias = list[
    "capo_application_discovery_service.types.delete_agent.DeleteAgent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAgents) -> list:
    import capo_application_discovery_service.types.delete_agent

    out: list = []
    for item in value:
        out.append(
            capo_application_discovery_service.types.delete_agent.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeleteAgents:
    import capo_application_discovery_service.types.delete_agent

    out: DeleteAgents = []
    for item in data:
        out.append(
            capo_application_discovery_service.types.delete_agent.deserialize_aws_json_1_1(
                item
            )
        )
    return out
