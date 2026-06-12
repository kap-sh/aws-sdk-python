"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListWorkflowsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.max_size100
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.status
    import aws_sdk_customer_profiles.types.timestamp
    import aws_sdk_customer_profiles.types.token
    import aws_sdk_customer_profiles.types.workflow_type


class ListWorkflowsRequest(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    workflow_type: NotRequired[
        "aws_sdk_customer_profiles.types.workflow_type.WorkflowType"
    ]
    """<p>The type of workflow. The only supported value is APPFLOW_INTEGRATION.</p>"""
    status: NotRequired["aws_sdk_customer_profiles.types.status.Status"]
    """<p>Status of workflow execution.</p>"""
    query_start_date: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>Retrieve workflows started after timestamp.</p>"""
    query_end_date: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>Retrieve workflows ended after timestamp.</p>"""
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowsRequest) -> dict:
    out: dict = {}
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
    if "query_start_date" in value:
        import aws_sdk_customer_profiles.types.timestamp

        out["QueryStartDate"] = (
            aws_sdk_customer_profiles.types.timestamp.serialize_json(
                value["query_start_date"]
            )
        )
    if "query_end_date" in value:
        import aws_sdk_customer_profiles.types.timestamp

        out["QueryEndDate"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
            value["query_end_date"]
        )
    return out


def deserialize_json(data: dict) -> ListWorkflowsRequest:
    out: ListWorkflowsRequest = {}  # type: ignore[typeddict-item]
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
    if "QueryStartDate" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["query_start_date"] = (
            aws_sdk_customer_profiles.types.timestamp.deserialize_json(
                data["QueryStartDate"]
            )
        )
    if "QueryEndDate" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["query_end_date"] = (
            aws_sdk_customer_profiles.types.timestamp.deserialize_json(
                data["QueryEndDate"]
            )
        )
    return out
