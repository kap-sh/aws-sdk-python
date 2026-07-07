"""Generated from Smithy shape ``com.amazonaws.securityagent#UpdateIntegratedResourcesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.agent_space_id
    import aws_sdk_securityagent.types.integrated_resource_input_item_list
    import aws_sdk_securityagent.types.integration_id


class UpdateIntegratedResourcesInput(TypedDict, closed=True):
    agent_space_id: "aws_sdk_securityagent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the agent space.</p>"""
    integration_id: "aws_sdk_securityagent.types.integration_id.IntegrationId"
    """<p>The unique identifier of the integration.</p>"""
    items: "aws_sdk_securityagent.types.integrated_resource_input_item_list.IntegratedResourceInputItemList"
    """<p>The list of integrated resource items to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIntegratedResourcesInput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    out["integrationId"] = value["integration_id"]
    import aws_sdk_securityagent.types.integrated_resource_input_item_list

    out["items"] = (
        aws_sdk_securityagent.types.integrated_resource_input_item_list.serialize_json(
            value["items"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateIntegratedResourcesInput:
    out: UpdateIntegratedResourcesInput = {}  # type: ignore[typeddict-item]
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError(
            "UpdateIntegratedResourcesInput.agent_space_id required"
        )
    if "integrationId" in data:
        out["integration_id"] = data["integrationId"]
    else:
        raise DeserializationError(
            "UpdateIntegratedResourcesInput.integration_id required"
        )
    if "items" in data:
        import aws_sdk_securityagent.types.integrated_resource_input_item_list

        out["items"] = (
            aws_sdk_securityagent.types.integrated_resource_input_item_list.deserialize_json(
                data["items"]
            )
        )
    else:
        raise DeserializationError("UpdateIntegratedResourcesInput.items required")
    return out
