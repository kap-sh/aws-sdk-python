"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#FlowExecutionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.flow_execution_id
    import capo_iotthingsgraph.types.flow_execution_status
    import capo_iotthingsgraph.types.timestamp
    import capo_iotthingsgraph.types.urn


class FlowExecutionSummary(TypedDict, closed=True):
    flow_execution_id: NotRequired[
        "capo_iotthingsgraph.types.flow_execution_id.FlowExecutionId"
    ]
    """<p>The ID of the flow execution.</p>"""
    status: NotRequired[
        "capo_iotthingsgraph.types.flow_execution_status.FlowExecutionStatus"
    ]
    """<p>The current status of the flow execution.</p>"""
    system_instance_id: NotRequired["capo_iotthingsgraph.types.urn.Urn"]
    """<p>The ID of the system instance that contains the flow.</p>"""
    flow_template_id: NotRequired["capo_iotthingsgraph.types.urn.Urn"]
    """<p>The ID of the flow.</p>"""
    created_at: NotRequired["capo_iotthingsgraph.types.timestamp.Timestamp"]
    """<p>The date and time when the flow execution summary was created.</p>"""
    updated_at: NotRequired["capo_iotthingsgraph.types.timestamp.Timestamp"]
    """<p>The date and time when the flow execution summary was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlowExecutionSummary) -> dict:
    out: dict = {}
    if "flow_execution_id" in value:
        out["flowExecutionId"] = value["flow_execution_id"]
    if "status" in value:
        import capo_iotthingsgraph.types.flow_execution_status

        out["status"] = (
            capo_iotthingsgraph.types.flow_execution_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "system_instance_id" in value:
        out["systemInstanceId"] = value["system_instance_id"]
    if "flow_template_id" in value:
        out["flowTemplateId"] = value["flow_template_id"]
    if "created_at" in value:
        import capo_iotthingsgraph.types.timestamp

        out["createdAt"] = capo_iotthingsgraph.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_iotthingsgraph.types.timestamp

        out["updatedAt"] = capo_iotthingsgraph.types.timestamp.serialize_aws_json_1_1(
            value["updated_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FlowExecutionSummary:
    out: FlowExecutionSummary = {}  # type: ignore[typeddict-item]
    if "flowExecutionId" in data:
        out["flow_execution_id"] = data["flowExecutionId"]
    if "status" in data:
        import capo_iotthingsgraph.types.flow_execution_status

        out["status"] = (
            capo_iotthingsgraph.types.flow_execution_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "systemInstanceId" in data:
        out["system_instance_id"] = data["systemInstanceId"]
    if "flowTemplateId" in data:
        out["flow_template_id"] = data["flowTemplateId"]
    if "createdAt" in data:
        import capo_iotthingsgraph.types.timestamp

        out["created_at"] = (
            capo_iotthingsgraph.types.timestamp.deserialize_aws_json_1_1(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import capo_iotthingsgraph.types.timestamp

        out["updated_at"] = (
            capo_iotthingsgraph.types.timestamp.deserialize_aws_json_1_1(
                data["updatedAt"]
            )
        )
    return out
