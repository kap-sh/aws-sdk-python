"""Generated from Smithy shape ``com.amazonaws.customerprofiles#WorkflowAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.appflow_integration_workflow_attributes


class WorkflowAttributes(TypedDict):
    appflow_integration: NotRequired[
        "aws_sdk_customer_profiles.types.appflow_integration_workflow_attributes.AppflowIntegrationWorkflowAttributes"
    ]
    """<p>Workflow attributes specific to <code>APPFLOW_INTEGRATION</code> workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowAttributes) -> dict:
    out: dict = {}
    if "appflow_integration" in value:
        import aws_sdk_customer_profiles.types.appflow_integration_workflow_attributes

        out["AppflowIntegration"] = (
            aws_sdk_customer_profiles.types.appflow_integration_workflow_attributes.serialize_json(
                value["appflow_integration"]
            )
        )
    return out


def deserialize_json(data: dict) -> WorkflowAttributes:
    out: WorkflowAttributes = {}  # type: ignore[typeddict-item]
    if "AppflowIntegration" in data:
        import aws_sdk_customer_profiles.types.appflow_integration_workflow_attributes

        out["appflow_integration"] = (
            aws_sdk_customer_profiles.types.appflow_integration_workflow_attributes.deserialize_json(
                data["AppflowIntegration"]
            )
        )
    return out
