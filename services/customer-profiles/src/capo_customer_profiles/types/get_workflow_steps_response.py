"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetWorkflowStepsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.token
    import capo_customer_profiles.types.uuid
    import capo_customer_profiles.types.workflow_steps_list
    import capo_customer_profiles.types.workflow_type


class GetWorkflowStepsResponse(TypedDict, closed=True):
    workflow_id: NotRequired["capo_customer_profiles.types.uuid.uuid"]
    """<p>Unique identifier for the workflow.</p>"""
    workflow_type: NotRequired[
        "capo_customer_profiles.types.workflow_type.WorkflowType"
    ]
    """<p>The type of workflow. The only supported value is APPFLOW_INTEGRATION.</p>"""
    items: NotRequired[
        "capo_customer_profiles.types.workflow_steps_list.WorkflowStepsList"
    ]
    """<p>List containing workflow step details.</p>"""
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkflowStepsResponse) -> dict:
    out: dict = {}
    if "workflow_id" in value:
        out["WorkflowId"] = value["workflow_id"]
    if "workflow_type" in value:
        import capo_customer_profiles.types.workflow_type

        out["WorkflowType"] = capo_customer_profiles.types.workflow_type.serialize_json(
            value["workflow_type"]
        )
    if "items" in value:
        import capo_customer_profiles.types.workflow_steps_list

        out["Items"] = capo_customer_profiles.types.workflow_steps_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetWorkflowStepsResponse:
    out: GetWorkflowStepsResponse = {}  # type: ignore[typeddict-item]
    if "WorkflowId" in data:
        out["workflow_id"] = data["WorkflowId"]
    if "WorkflowType" in data:
        import capo_customer_profiles.types.workflow_type

        out["workflow_type"] = (
            capo_customer_profiles.types.workflow_type.deserialize_json(
                data["WorkflowType"]
            )
        )
    if "Items" in data:
        import capo_customer_profiles.types.workflow_steps_list

        out["items"] = (
            capo_customer_profiles.types.workflow_steps_list.deserialize_json(
                data["Items"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
