"""Generated from Smithy shape ``com.amazonaws.mturk#ListBonusPaymentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mturk.types.entity_id
    import aws_sdk_mturk.types.pagination_token
    import aws_sdk_mturk.types.result_size


class ListBonusPaymentsRequest(TypedDict, closed=True):
    hit_id: NotRequired["aws_sdk_mturk.types.entity_id.EntityId"]
    """<p>The ID of the HIT associated with the bonus payments to retrieve. If not specified, all bonus payments for all assignments for the given HIT are returned. Either the HITId parameter or the AssignmentId parameter must be specified</p>"""
    assignment_id: NotRequired["aws_sdk_mturk.types.entity_id.EntityId"]
    """<p>The ID of the assignment associated with the bonus payments to retrieve. If specified, only bonus payments for the given assignment are returned. Either the HITId parameter or the AssignmentId parameter must be specified</p>"""
    next_token: NotRequired["aws_sdk_mturk.types.pagination_token.PaginationToken"]
    """<p>Pagination token</p>"""
    max_results: NotRequired["aws_sdk_mturk.types.result_size.ResultSize"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListBonusPaymentsRequest) -> dict:
    out: dict = {}
    if "hit_id" in value:
        out["HITId"] = value["hit_id"]
    if "assignment_id" in value:
        out["AssignmentId"] = value["assignment_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListBonusPaymentsRequest:
    out: ListBonusPaymentsRequest = {}  # type: ignore[typeddict-item]
    if "HITId" in data:
        out["hit_id"] = data["HITId"]
    if "AssignmentId" in data:
        out["assignment_id"] = data["AssignmentId"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
