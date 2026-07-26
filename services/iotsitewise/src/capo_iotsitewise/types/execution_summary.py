"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ExecutionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.execution_status
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name
    import capo_iotsitewise.types.resolve_to
    import capo_iotsitewise.types.target_resource
    import capo_iotsitewise.types.timestamp
    import capo_iotsitewise.types.version


class ExecutionSummary(TypedDict, closed=True):
    execution_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the execution.</p>"""
    action_type: NotRequired["capo_iotsitewise.types.name.Name"]
    """<p>The type of action exectued.</p>"""
    target_resource: "capo_iotsitewise.types.target_resource.TargetResource"
    target_resource_version: "capo_iotsitewise.types.version.Version"
    """<p>The version of the target resource.</p>"""
    resolve_to: NotRequired["capo_iotsitewise.types.resolve_to.ResolveTo"]
    """<p>The detailed resource this execution resolves to.</p>"""
    execution_start_time: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The time the process started.</p>"""
    execution_end_time: NotRequired["capo_iotsitewise.types.timestamp.Timestamp"]
    """<p>The time the process ended.</p>"""
    execution_status: "capo_iotsitewise.types.execution_status.ExecutionStatus"
    """<p>The status of the execution process.</p>"""
    execution_entity_version: NotRequired["capo_iotsitewise.types.version.Version"]
    """<p>The execution entity version associated with the summary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionSummary) -> dict:
    out: dict = {}
    out["executionId"] = value["execution_id"]
    if "action_type" in value:
        out["actionType"] = value["action_type"]
    import capo_iotsitewise.types.target_resource

    out["targetResource"] = capo_iotsitewise.types.target_resource.serialize_json(
        value["target_resource"]
    )
    out["targetResourceVersion"] = value["target_resource_version"]
    if "resolve_to" in value:
        import capo_iotsitewise.types.resolve_to

        out["resolveTo"] = capo_iotsitewise.types.resolve_to.serialize_json(
            value["resolve_to"]
        )
    import capo_iotsitewise.types.timestamp

    out["executionStartTime"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["execution_start_time"]
    )
    if "execution_end_time" in value:
        import capo_iotsitewise.types.timestamp

        out["executionEndTime"] = capo_iotsitewise.types.timestamp.serialize_json(
            value["execution_end_time"]
        )
    import capo_iotsitewise.types.execution_status

    out["executionStatus"] = capo_iotsitewise.types.execution_status.serialize_json(
        value["execution_status"]
    )
    if "execution_entity_version" in value:
        out["executionEntityVersion"] = value["execution_entity_version"]
    return out


def deserialize_json(data: dict) -> ExecutionSummary:
    out: ExecutionSummary = {}  # type: ignore[typeddict-item]
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    else:
        raise DeserializationError("ExecutionSummary.execution_id required")
    if "actionType" in data:
        out["action_type"] = data["actionType"]
    if "targetResource" in data:
        import capo_iotsitewise.types.target_resource

        out["target_resource"] = (
            capo_iotsitewise.types.target_resource.deserialize_json(
                data["targetResource"]
            )
        )
    else:
        raise DeserializationError("ExecutionSummary.target_resource required")
    if "targetResourceVersion" in data:
        out["target_resource_version"] = data["targetResourceVersion"]
    else:
        raise DeserializationError("ExecutionSummary.target_resource_version required")
    if "resolveTo" in data:
        import capo_iotsitewise.types.resolve_to

        out["resolve_to"] = capo_iotsitewise.types.resolve_to.deserialize_json(
            data["resolveTo"]
        )
    if "executionStartTime" in data:
        import capo_iotsitewise.types.timestamp

        out["execution_start_time"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["executionStartTime"]
        )
    else:
        raise DeserializationError("ExecutionSummary.execution_start_time required")
    if "executionEndTime" in data:
        import capo_iotsitewise.types.timestamp

        out["execution_end_time"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["executionEndTime"]
        )
    if "executionStatus" in data:
        import capo_iotsitewise.types.execution_status

        out["execution_status"] = (
            capo_iotsitewise.types.execution_status.deserialize_json(
                data["executionStatus"]
            )
        )
    else:
        raise DeserializationError("ExecutionSummary.execution_status required")
    if "executionEntityVersion" in data:
        out["execution_entity_version"] = data["executionEntityVersion"]
    return out
