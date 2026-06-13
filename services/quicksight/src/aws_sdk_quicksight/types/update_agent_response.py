"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateAgentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.agent_arn
    import aws_sdk_quicksight.types.agent_id
    import aws_sdk_quicksight.types.agent_status
    import aws_sdk_quicksight.types.failed_to_update_association_list


class UpdateAgentResponse(TypedDict):
    arn: "aws_sdk_quicksight.types.agent_arn.AgentArn"
    """<p>The Amazon Resource Name (ARN) of the agent.</p>"""
    agent_id: "aws_sdk_quicksight.types.agent_id.AgentId"
    """<p>The unique identifier for the agent.</p>"""
    agent_status: "aws_sdk_quicksight.types.agent_status.AgentStatus"
    """<p>The status of the agent.</p>"""
    failed_to_add_spaces: NotRequired[
        "aws_sdk_quicksight.types.failed_to_update_association_list.FailedToUpdateAssociationList"
    ]
    """<p>A list of per-ARN failures from the spaces that were requested to be added.</p>"""
    failed_to_remove_spaces: NotRequired[
        "aws_sdk_quicksight.types.failed_to_update_association_list.FailedToUpdateAssociationList"
    ]
    """<p>A list of per-ARN failures from the spaces that were requested to be removed.</p>"""
    failed_to_add_action_connectors: NotRequired[
        "aws_sdk_quicksight.types.failed_to_update_association_list.FailedToUpdateAssociationList"
    ]
    """<p>A list of per-ARN failures from the action connectors that were requested to be added.</p>"""
    failed_to_remove_action_connectors: NotRequired[
        "aws_sdk_quicksight.types.failed_to_update_association_list.FailedToUpdateAssociationList"
    ]
    """<p>A list of per-ARN failures from the action connectors that were requested to be removed.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentResponse) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["AgentId"] = value["agent_id"]
    import aws_sdk_quicksight.types.agent_status

    out["AgentStatus"] = aws_sdk_quicksight.types.agent_status.serialize_json(
        value["agent_status"]
    )
    if "failed_to_add_spaces" in value:
        import aws_sdk_quicksight.types.failed_to_update_association_list

        out["FailedToAddSpaces"] = (
            aws_sdk_quicksight.types.failed_to_update_association_list.serialize_json(
                value["failed_to_add_spaces"]
            )
        )
    if "failed_to_remove_spaces" in value:
        import aws_sdk_quicksight.types.failed_to_update_association_list

        out["FailedToRemoveSpaces"] = (
            aws_sdk_quicksight.types.failed_to_update_association_list.serialize_json(
                value["failed_to_remove_spaces"]
            )
        )
    if "failed_to_add_action_connectors" in value:
        import aws_sdk_quicksight.types.failed_to_update_association_list

        out["FailedToAddActionConnectors"] = (
            aws_sdk_quicksight.types.failed_to_update_association_list.serialize_json(
                value["failed_to_add_action_connectors"]
            )
        )
    if "failed_to_remove_action_connectors" in value:
        import aws_sdk_quicksight.types.failed_to_update_association_list

        out["FailedToRemoveActionConnectors"] = (
            aws_sdk_quicksight.types.failed_to_update_association_list.serialize_json(
                value["failed_to_remove_action_connectors"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateAgentResponse:
    out: UpdateAgentResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("UpdateAgentResponse.arn required")
    if "AgentId" in data:
        out["agent_id"] = data["AgentId"]
    else:
        raise DeserializationError("UpdateAgentResponse.agent_id required")
    if "AgentStatus" in data:
        import aws_sdk_quicksight.types.agent_status

        out["agent_status"] = aws_sdk_quicksight.types.agent_status.deserialize_json(
            data["AgentStatus"]
        )
    else:
        raise DeserializationError("UpdateAgentResponse.agent_status required")
    if "FailedToAddSpaces" in data:
        import aws_sdk_quicksight.types.failed_to_update_association_list

        out["failed_to_add_spaces"] = (
            aws_sdk_quicksight.types.failed_to_update_association_list.deserialize_json(
                data["FailedToAddSpaces"]
            )
        )
    if "FailedToRemoveSpaces" in data:
        import aws_sdk_quicksight.types.failed_to_update_association_list

        out["failed_to_remove_spaces"] = (
            aws_sdk_quicksight.types.failed_to_update_association_list.deserialize_json(
                data["FailedToRemoveSpaces"]
            )
        )
    if "FailedToAddActionConnectors" in data:
        import aws_sdk_quicksight.types.failed_to_update_association_list

        out["failed_to_add_action_connectors"] = (
            aws_sdk_quicksight.types.failed_to_update_association_list.deserialize_json(
                data["FailedToAddActionConnectors"]
            )
        )
    if "FailedToRemoveActionConnectors" in data:
        import aws_sdk_quicksight.types.failed_to_update_association_list

        out["failed_to_remove_action_connectors"] = (
            aws_sdk_quicksight.types.failed_to_update_association_list.deserialize_json(
                data["FailedToRemoveActionConnectors"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
