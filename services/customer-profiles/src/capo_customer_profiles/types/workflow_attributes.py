"""Generated from Smithy shape ``com.amazonaws.customerprofiles#WorkflowAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.appflow_integration_workflow_attributes


class WorkflowAttributes(TypedDict, closed=True):
    appflow_integration: NotRequired[
        "capo_customer_profiles.types.appflow_integration_workflow_attributes.AppflowIntegrationWorkflowAttributes"
    ]
    """<p>Workflow attributes specific to <code>APPFLOW_INTEGRATION</code> workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowAttributes) -> dict:
    out: dict = {}
    if "appflow_integration" in value:
        import capo_customer_profiles.types.appflow_integration_workflow_attributes

        out["AppflowIntegration"] = (
            capo_customer_profiles.types.appflow_integration_workflow_attributes.serialize_json(
                value["appflow_integration"]
            )
        )
    return out


def deserialize_json(data: dict) -> WorkflowAttributes:
    out: WorkflowAttributes = {}  # type: ignore[typeddict-item]
    if "AppflowIntegration" in data:
        import capo_customer_profiles.types.appflow_integration_workflow_attributes

        out["appflow_integration"] = (
            capo_customer_profiles.types.appflow_integration_workflow_attributes.deserialize_json(
                data["AppflowIntegration"]
            )
        )
    return out
