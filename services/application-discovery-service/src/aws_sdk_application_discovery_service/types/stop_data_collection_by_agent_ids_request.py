"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#StopDataCollectionByAgentIdsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_application_discovery_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.agent_ids


class StopDataCollectionByAgentIdsRequest(TypedDict):
    agent_ids: "aws_sdk_application_discovery_service.types.agent_ids.AgentIds"
    """<p>The IDs of the agents from which to stop collecting data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopDataCollectionByAgentIdsRequest) -> dict:
    out: dict = {}
    import aws_sdk_application_discovery_service.types.agent_ids

    out["agentIds"] = (
        aws_sdk_application_discovery_service.types.agent_ids.serialize_aws_json_1_1(
            value["agent_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopDataCollectionByAgentIdsRequest:
    out: StopDataCollectionByAgentIdsRequest = {}  # type: ignore[typeddict-item]
    if "agentIds" in data:
        import aws_sdk_application_discovery_service.types.agent_ids

        out["agent_ids"] = (
            aws_sdk_application_discovery_service.types.agent_ids.deserialize_aws_json_1_1(
                data["agentIds"]
            )
        )
    else:
        raise DeserializationError(
            "StopDataCollectionByAgentIdsRequest.agent_ids required"
        )
    return out
