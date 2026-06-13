"""Generated from Smithy shape ``com.amazonaws.groundstation#UpdateAgentStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.aggregate_status
    import aws_sdk_groundstation.types.component_status_list
    import aws_sdk_groundstation.types.uuid


class UpdateAgentStatusRequest(TypedDict):
    agent_id: "aws_sdk_groundstation.types.uuid.Uuid"
    """<p>UUID of agent to update.</p>"""
    task_id: "aws_sdk_groundstation.types.uuid.Uuid"
    """<p>GUID of agent task.</p>"""
    aggregate_status: "aws_sdk_groundstation.types.aggregate_status.AggregateStatus"
    """<p>Aggregate status for agent.</p>"""
    component_statuses: (
        "aws_sdk_groundstation.types.component_status_list.ComponentStatusList"
    )
    """<p>List of component statuses for agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentStatusRequest) -> dict:
    out: dict = {}
    out["taskId"] = value["task_id"]
    import aws_sdk_groundstation.types.aggregate_status

    out["aggregateStatus"] = (
        aws_sdk_groundstation.types.aggregate_status.serialize_json(
            value["aggregate_status"]
        )
    )
    import aws_sdk_groundstation.types.component_status_list

    out["componentStatuses"] = (
        aws_sdk_groundstation.types.component_status_list.serialize_json(
            value["component_statuses"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateAgentStatusRequest:
    out: UpdateAgentStatusRequest = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    else:
        raise DeserializationError("UpdateAgentStatusRequest.task_id required")
    if "aggregateStatus" in data:
        import aws_sdk_groundstation.types.aggregate_status

        out["aggregate_status"] = (
            aws_sdk_groundstation.types.aggregate_status.deserialize_json(
                data["aggregateStatus"]
            )
        )
    else:
        raise DeserializationError("UpdateAgentStatusRequest.aggregate_status required")
    if "componentStatuses" in data:
        import aws_sdk_groundstation.types.component_status_list

        out["component_statuses"] = (
            aws_sdk_groundstation.types.component_status_list.deserialize_json(
                data["componentStatuses"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAgentStatusRequest.component_statuses required"
        )
    return out
