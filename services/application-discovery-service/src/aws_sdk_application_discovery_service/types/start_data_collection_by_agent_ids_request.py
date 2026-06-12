"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#StartDataCollectionByAgentIdsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_application_discovery_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.agent_ids


class StartDataCollectionByAgentIdsRequest(TypedDict):
    agent_ids: "aws_sdk_application_discovery_service.types.agent_ids.AgentIds"
    """<p>The IDs of the agents from which to start collecting data. If you send a request to an agent ID that you do not have permission to contact, according to your Amazon Web Services account, the service does not throw an exception. Instead, it returns the error in the <i>Description</i> field. If you send a request to multiple agents and you do not have permission to contact some of those agents, the system does not throw an exception. Instead, the system shows <code>Failed</code> in the <i>Description</i> field.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartDataCollectionByAgentIdsRequest) -> dict:
    out: dict = {}
    import aws_sdk_application_discovery_service.types.agent_ids

    out["agentIds"] = (
        aws_sdk_application_discovery_service.types.agent_ids.serialize_aws_json_1_1(
            value["agent_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartDataCollectionByAgentIdsRequest:
    out: StartDataCollectionByAgentIdsRequest = {}  # type: ignore[typeddict-item]
    if "agentIds" in data:
        import aws_sdk_application_discovery_service.types.agent_ids

        out["agent_ids"] = (
            aws_sdk_application_discovery_service.types.agent_ids.deserialize_aws_json_1_1(
                data["agentIds"]
            )
        )
    else:
        raise DeserializationError(
            "StartDataCollectionByAgentIdsRequest.agent_ids required"
        )
    return out
