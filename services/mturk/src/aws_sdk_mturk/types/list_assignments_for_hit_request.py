"""Generated from Smithy shape ``com.amazonaws.mturk#ListAssignmentsForHITRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mturk.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mturk.types.assignment_status_list
    import aws_sdk_mturk.types.entity_id
    import aws_sdk_mturk.types.pagination_token
    import aws_sdk_mturk.types.result_size


class ListAssignmentsForHITRequest(TypedDict):
    hit_id: "aws_sdk_mturk.types.entity_id.EntityId"
    """<p>The ID of the HIT.</p>"""
    next_token: NotRequired["aws_sdk_mturk.types.pagination_token.PaginationToken"]
    """<p>Pagination token</p>"""
    max_results: NotRequired["aws_sdk_mturk.types.result_size.ResultSize"]
    assignment_statuses: NotRequired[
        "aws_sdk_mturk.types.assignment_status_list.AssignmentStatusList"
    ]
    """<p>The status of the assignments to return: Submitted | Approved | Rejected</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAssignmentsForHITRequest) -> dict:
    out: dict = {}
    out["HITId"] = value["hit_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "assignment_statuses" in value:
        import aws_sdk_mturk.types.assignment_status_list

        out["AssignmentStatuses"] = (
            aws_sdk_mturk.types.assignment_status_list.serialize_aws_json_1_1(
                value["assignment_statuses"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAssignmentsForHITRequest:
    out: ListAssignmentsForHITRequest = {}  # type: ignore[typeddict-item]
    if "HITId" in data:
        out["hit_id"] = data["HITId"]
    else:
        raise DeserializationError("ListAssignmentsForHITRequest.hit_id required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "AssignmentStatuses" in data:
        import aws_sdk_mturk.types.assignment_status_list

        out["assignment_statuses"] = (
            aws_sdk_mturk.types.assignment_status_list.deserialize_aws_json_1_1(
                data["AssignmentStatuses"]
            )
        )
    return out
