"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListWorkflowsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.max_size100
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.status
    import capo_customer_profiles.types.timestamp
    import capo_customer_profiles.types.token
    import capo_customer_profiles.types.workflow_type


class ListWorkflowsRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    workflow_type: NotRequired[
        "capo_customer_profiles.types.workflow_type.WorkflowType"
    ]
    """<p>The type of workflow. The only supported value is APPFLOW_INTEGRATION.</p>"""
    status: NotRequired["capo_customer_profiles.types.status.Status"]
    """<p>Status of workflow execution.</p>"""
    query_start_date: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>Retrieve workflows started after timestamp.</p>"""
    query_end_date: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>Retrieve workflows ended after timestamp.</p>"""
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowsRequest) -> dict:
    out: dict = {}
    if "workflow_type" in value:
        import capo_customer_profiles.types.workflow_type

        out["WorkflowType"] = capo_customer_profiles.types.workflow_type.serialize_json(
            value["workflow_type"]
        )
    if "status" in value:
        import capo_customer_profiles.types.status

        out["Status"] = capo_customer_profiles.types.status.serialize_json(
            value["status"]
        )
    if "query_start_date" in value:
        import capo_customer_profiles.types.timestamp

        out["QueryStartDate"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["query_start_date"]
        )
    if "query_end_date" in value:
        import capo_customer_profiles.types.timestamp

        out["QueryEndDate"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["query_end_date"]
        )
    return out


def deserialize_json(data: dict) -> ListWorkflowsRequest:
    out: ListWorkflowsRequest = {}  # type: ignore[typeddict-item]
    if "WorkflowType" in data:
        import capo_customer_profiles.types.workflow_type

        out["workflow_type"] = (
            capo_customer_profiles.types.workflow_type.deserialize_json(
                data["WorkflowType"]
            )
        )
    if "Status" in data:
        import capo_customer_profiles.types.status

        out["status"] = capo_customer_profiles.types.status.deserialize_json(
            data["Status"]
        )
    if "QueryStartDate" in data:
        import capo_customer_profiles.types.timestamp

        out["query_start_date"] = (
            capo_customer_profiles.types.timestamp.deserialize_json(
                data["QueryStartDate"]
            )
        )
    if "QueryEndDate" in data:
        import capo_customer_profiles.types.timestamp

        out["query_end_date"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["QueryEndDate"]
        )
    return out
