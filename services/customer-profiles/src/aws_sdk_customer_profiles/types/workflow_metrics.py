"""Generated from Smithy shape ``com.amazonaws.customerprofiles#WorkflowMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.appflow_integration_workflow_metrics


class WorkflowMetrics(TypedDict, closed=True):
    appflow_integration: NotRequired[
        "aws_sdk_customer_profiles.types.appflow_integration_workflow_metrics.AppflowIntegrationWorkflowMetrics"
    ]
    """<p>Workflow execution metrics for <code>APPFLOW_INTEGRATION</code> workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowMetrics) -> dict:
    out: dict = {}
    if "appflow_integration" in value:
        import aws_sdk_customer_profiles.types.appflow_integration_workflow_metrics

        out["AppflowIntegration"] = (
            aws_sdk_customer_profiles.types.appflow_integration_workflow_metrics.serialize_json(
                value["appflow_integration"]
            )
        )
    return out


def deserialize_json(data: dict) -> WorkflowMetrics:
    out: WorkflowMetrics = {}  # type: ignore[typeddict-item]
    if "AppflowIntegration" in data:
        import aws_sdk_customer_profiles.types.appflow_integration_workflow_metrics

        out["appflow_integration"] = (
            aws_sdk_customer_profiles.types.appflow_integration_workflow_metrics.deserialize_json(
                data["AppflowIntegration"]
            )
        )
    return out
