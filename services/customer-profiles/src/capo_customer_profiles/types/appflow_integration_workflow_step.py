"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AppflowIntegrationWorkflowStep``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.flow_name
    import capo_customer_profiles.types.long
    import capo_customer_profiles.types.status
    import capo_customer_profiles.types.string1_to255
    import capo_customer_profiles.types.timestamp


class AppflowIntegrationWorkflowStep(TypedDict, closed=True):
    flow_name: "capo_customer_profiles.types.flow_name.FlowName"
    """<p>Name of the flow created during execution of workflow step. <code>APPFLOW_INTEGRATION</code> workflow type creates an appflow flow during workflow step execution on the customers behalf.</p>"""
    status: "capo_customer_profiles.types.status.Status"
    """<p>Workflow step status for <code>APPFLOW_INTEGRATION</code> workflow.</p>"""
    execution_message: "capo_customer_profiles.types.string1_to255.string1To255"
    """<p>Message indicating execution of workflow step for <code>APPFLOW_INTEGRATION</code> workflow.</p>"""
    records_processed: "capo_customer_profiles.types.long.long"
    """<p>Total number of records processed during execution of workflow step for <code>APPFLOW_INTEGRATION</code> workflow.</p>"""
    batch_records_start_time: "capo_customer_profiles.types.string1_to255.string1To255"
    """<p>Start datetime of records pulled in batch during execution of workflow step for <code>APPFLOW_INTEGRATION</code> workflow.</p>"""
    batch_records_end_time: "capo_customer_profiles.types.string1_to255.string1To255"
    """<p>End datetime of records pulled in batch during execution of workflow step for <code>APPFLOW_INTEGRATION</code> workflow.</p>"""
    created_at: "capo_customer_profiles.types.timestamp.timestamp"
    """<p>Creation timestamp of workflow step for <code>APPFLOW_INTEGRATION</code> workflow.</p>"""
    last_updated_at: "capo_customer_profiles.types.timestamp.timestamp"
    """<p>Last updated timestamp for workflow step for <code>APPFLOW_INTEGRATION</code> workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppflowIntegrationWorkflowStep) -> dict:
    out: dict = {}
    out["FlowName"] = value["flow_name"]
    import capo_customer_profiles.types.status

    out["Status"] = capo_customer_profiles.types.status.serialize_json(value["status"])
    out["ExecutionMessage"] = value["execution_message"]
    out["RecordsProcessed"] = value.get("records_processed", 0)
    out["BatchRecordsStartTime"] = value["batch_records_start_time"]
    out["BatchRecordsEndTime"] = value["batch_records_end_time"]
    import capo_customer_profiles.types.timestamp

    out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_customer_profiles.types.timestamp

    out["LastUpdatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
        value["last_updated_at"]
    )
    return out


def deserialize_json(data: dict) -> AppflowIntegrationWorkflowStep:
    out: AppflowIntegrationWorkflowStep = {}  # type: ignore[typeddict-item]
    if "FlowName" in data:
        out["flow_name"] = data["FlowName"]
    else:
        raise DeserializationError("AppflowIntegrationWorkflowStep.flow_name required")
    if "Status" in data:
        import capo_customer_profiles.types.status

        out["status"] = capo_customer_profiles.types.status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("AppflowIntegrationWorkflowStep.status required")
    if "ExecutionMessage" in data:
        out["execution_message"] = data["ExecutionMessage"]
    else:
        raise DeserializationError(
            "AppflowIntegrationWorkflowStep.execution_message required"
        )
    if "RecordsProcessed" in data:
        out["records_processed"] = data["RecordsProcessed"]
    else:
        out["records_processed"] = 0
    if "BatchRecordsStartTime" in data:
        out["batch_records_start_time"] = data["BatchRecordsStartTime"]
    else:
        raise DeserializationError(
            "AppflowIntegrationWorkflowStep.batch_records_start_time required"
        )
    if "BatchRecordsEndTime" in data:
        out["batch_records_end_time"] = data["BatchRecordsEndTime"]
    else:
        raise DeserializationError(
            "AppflowIntegrationWorkflowStep.batch_records_end_time required"
        )
    if "CreatedAt" in data:
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        raise DeserializationError("AppflowIntegrationWorkflowStep.created_at required")
    if "LastUpdatedAt" in data:
        import capo_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            capo_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "AppflowIntegrationWorkflowStep.last_updated_at required"
        )
    return out
