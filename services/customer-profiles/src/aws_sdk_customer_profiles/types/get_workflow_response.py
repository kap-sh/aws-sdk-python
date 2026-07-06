"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetWorkflowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.status
    import aws_sdk_customer_profiles.types.string1_to255
    import aws_sdk_customer_profiles.types.timestamp
    import aws_sdk_customer_profiles.types.uuid
    import aws_sdk_customer_profiles.types.workflow_attributes
    import aws_sdk_customer_profiles.types.workflow_metrics
    import aws_sdk_customer_profiles.types.workflow_type


class GetWorkflowResponse(TypedDict, closed=True):
    workflow_id: NotRequired["aws_sdk_customer_profiles.types.uuid.uuid"]
    """<p>Unique identifier for the workflow.</p>"""
    workflow_type: NotRequired[
        "aws_sdk_customer_profiles.types.workflow_type.WorkflowType"
    ]
    """<p>The type of workflow. The only supported value is APPFLOW_INTEGRATION.</p>"""
    status: NotRequired["aws_sdk_customer_profiles.types.status.Status"]
    """<p>Status of workflow execution.</p>"""
    error_description: NotRequired[
        "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    ]
    """<p>Workflow error messages during execution (if any).</p>"""
    start_date: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp that represents when workflow execution started.</p>"""
    last_updated_at: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp that represents when workflow execution last updated.</p>"""
    attributes: NotRequired[
        "aws_sdk_customer_profiles.types.workflow_attributes.WorkflowAttributes"
    ]
    """<p>Attributes provided for workflow execution.</p>"""
    metrics: NotRequired[
        "aws_sdk_customer_profiles.types.workflow_metrics.WorkflowMetrics"
    ]
    """<p>Workflow specific execution metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkflowResponse) -> dict:
    out: dict = {}
    if "workflow_id" in value:
        out["WorkflowId"] = value["workflow_id"]
    if "workflow_type" in value:
        import aws_sdk_customer_profiles.types.workflow_type

        out["WorkflowType"] = (
            aws_sdk_customer_profiles.types.workflow_type.serialize_json(
                value["workflow_type"]
            )
        )
    if "status" in value:
        import aws_sdk_customer_profiles.types.status

        out["Status"] = aws_sdk_customer_profiles.types.status.serialize_json(
            value["status"]
        )
    if "error_description" in value:
        out["ErrorDescription"] = value["error_description"]
    if "start_date" in value:
        import aws_sdk_customer_profiles.types.timestamp

        out["StartDate"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
            value["start_date"]
        )
    if "last_updated_at" in value:
        import aws_sdk_customer_profiles.types.timestamp

        out["LastUpdatedAt"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "attributes" in value:
        import aws_sdk_customer_profiles.types.workflow_attributes

        out["Attributes"] = (
            aws_sdk_customer_profiles.types.workflow_attributes.serialize_json(
                value["attributes"]
            )
        )
    if "metrics" in value:
        import aws_sdk_customer_profiles.types.workflow_metrics

        out["Metrics"] = (
            aws_sdk_customer_profiles.types.workflow_metrics.serialize_json(
                value["metrics"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetWorkflowResponse:
    out: GetWorkflowResponse = {}  # type: ignore[typeddict-item]
    if "WorkflowId" in data:
        out["workflow_id"] = data["WorkflowId"]
    if "WorkflowType" in data:
        import aws_sdk_customer_profiles.types.workflow_type

        out["workflow_type"] = (
            aws_sdk_customer_profiles.types.workflow_type.deserialize_json(
                data["WorkflowType"]
            )
        )
    if "Status" in data:
        import aws_sdk_customer_profiles.types.status

        out["status"] = aws_sdk_customer_profiles.types.status.deserialize_json(
            data["Status"]
        )
    if "ErrorDescription" in data:
        out["error_description"] = data["ErrorDescription"]
    if "StartDate" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["start_date"] = aws_sdk_customer_profiles.types.timestamp.deserialize_json(
            data["StartDate"]
        )
    if "LastUpdatedAt" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            aws_sdk_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    if "Attributes" in data:
        import aws_sdk_customer_profiles.types.workflow_attributes

        out["attributes"] = (
            aws_sdk_customer_profiles.types.workflow_attributes.deserialize_json(
                data["Attributes"]
            )
        )
    if "Metrics" in data:
        import aws_sdk_customer_profiles.types.workflow_metrics

        out["metrics"] = (
            aws_sdk_customer_profiles.types.workflow_metrics.deserialize_json(
                data["Metrics"]
            )
        )
    return out
