"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AppflowIntegrationWorkflowMetrics``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.long


class AppflowIntegrationWorkflowMetrics(TypedDict):
    records_processed: "aws_sdk_customer_profiles.types.long.long"
    """<p>Number of records processed in <code>APPFLOW_INTEGRATION</code> workflow.</p>"""
    steps_completed: "aws_sdk_customer_profiles.types.long.long"
    """<p>Total steps completed in <code>APPFLOW_INTEGRATION</code> workflow.</p>"""
    total_steps: "aws_sdk_customer_profiles.types.long.long"
    """<p>Total steps in <code>APPFLOW_INTEGRATION</code> workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppflowIntegrationWorkflowMetrics) -> dict:
    out: dict = {}
    out["RecordsProcessed"] = value.get("records_processed", 0)
    out["StepsCompleted"] = value.get("steps_completed", 0)
    out["TotalSteps"] = value.get("total_steps", 0)
    return out


def deserialize_json(data: dict) -> AppflowIntegrationWorkflowMetrics:
    out: AppflowIntegrationWorkflowMetrics = {}  # type: ignore[typeddict-item]
    if "RecordsProcessed" in data:
        out["records_processed"] = data["RecordsProcessed"]
    else:
        out["records_processed"] = 0
    if "StepsCompleted" in data:
        out["steps_completed"] = data["StepsCompleted"]
    else:
        out["steps_completed"] = 0
    if "TotalSteps" in data:
        out["total_steps"] = data["TotalSteps"]
    else:
        out["total_steps"] = 0
    return out
