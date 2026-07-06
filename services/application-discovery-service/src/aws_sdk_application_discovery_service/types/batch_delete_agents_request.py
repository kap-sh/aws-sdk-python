"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#BatchDeleteAgentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_application_discovery_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.delete_agents


class BatchDeleteAgentsRequest(TypedDict, closed=True):
    delete_agents: (
        "aws_sdk_application_discovery_service.types.delete_agents.DeleteAgents"
    )
    """<p> The list of agents to delete. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteAgentsRequest) -> dict:
    out: dict = {}
    import aws_sdk_application_discovery_service.types.delete_agents

    out["deleteAgents"] = (
        aws_sdk_application_discovery_service.types.delete_agents.serialize_aws_json_1_1(
            value["delete_agents"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteAgentsRequest:
    out: BatchDeleteAgentsRequest = {}  # type: ignore[typeddict-item]
    if "deleteAgents" in data:
        import aws_sdk_application_discovery_service.types.delete_agents

        out["delete_agents"] = (
            aws_sdk_application_discovery_service.types.delete_agents.deserialize_aws_json_1_1(
                data["deleteAgents"]
            )
        )
    else:
        raise DeserializationError("BatchDeleteAgentsRequest.delete_agents required")
    return out
