"""Generated from Smithy shape ``com.amazonaws.mturk#ListAssignmentsForHITResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.assignment_list
    import capo_mturk.types.integer
    import capo_mturk.types.pagination_token


class ListAssignmentsForHITResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_mturk.types.pagination_token.PaginationToken"]
    num_results: NotRequired["capo_mturk.types.integer.Integer"]
    """<p> The number of assignments on the page in the filtered results list, equivalent to the number of assignments returned by this call.</p>"""
    assignments: NotRequired["capo_mturk.types.assignment_list.AssignmentList"]
    """<p> The collection of Assignment data structures returned by this call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAssignmentsForHITResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "num_results" in value:
        out["NumResults"] = value["num_results"]
    if "assignments" in value:
        import capo_mturk.types.assignment_list

        out["Assignments"] = capo_mturk.types.assignment_list.serialize_aws_json_1_1(
            value["assignments"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAssignmentsForHITResponse:
    out: ListAssignmentsForHITResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "NumResults" in data:
        out["num_results"] = data["NumResults"]
    if "Assignments" in data:
        import capo_mturk.types.assignment_list

        out["assignments"] = capo_mturk.types.assignment_list.deserialize_aws_json_1_1(
            data["Assignments"]
        )
    return out
