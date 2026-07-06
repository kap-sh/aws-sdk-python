"""Generated from Smithy shape ``com.amazonaws.customerprofiles#WorkflowStepItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.appflow_integration_workflow_step


class WorkflowStepItem(TypedDict, closed=True):
    appflow_integration: NotRequired[
        "aws_sdk_customer_profiles.types.appflow_integration_workflow_step.AppflowIntegrationWorkflowStep"
    ]
    """<p>Workflow step information specific to <code>APPFLOW_INTEGRATION</code> workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowStepItem) -> dict:
    out: dict = {}
    if "appflow_integration" in value:
        import aws_sdk_customer_profiles.types.appflow_integration_workflow_step

        out["AppflowIntegration"] = (
            aws_sdk_customer_profiles.types.appflow_integration_workflow_step.serialize_json(
                value["appflow_integration"]
            )
        )
    return out


def deserialize_json(data: dict) -> WorkflowStepItem:
    out: WorkflowStepItem = {}  # type: ignore[typeddict-item]
    if "AppflowIntegration" in data:
        import aws_sdk_customer_profiles.types.appflow_integration_workflow_step

        out["appflow_integration"] = (
            aws_sdk_customer_profiles.types.appflow_integration_workflow_step.deserialize_json(
                data["AppflowIntegration"]
            )
        )
    return out
