"""Generated from Smithy shape ``com.amazonaws.mturk#ListQualificationRequestsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.integer
    import capo_mturk.types.pagination_token
    import capo_mturk.types.qualification_request_list


class ListQualificationRequestsResponse(TypedDict, closed=True):
    num_results: NotRequired["capo_mturk.types.integer.Integer"]
    """<p>The number of Qualification requests on this page in the filtered results list, equivalent to the number of Qualification requests being returned by this call.</p>"""
    next_token: NotRequired["capo_mturk.types.pagination_token.PaginationToken"]
    qualification_requests: NotRequired[
        "capo_mturk.types.qualification_request_list.QualificationRequestList"
    ]
    """<p>The Qualification request. The response includes one QualificationRequest element for each Qualification request returned by the query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListQualificationRequestsResponse) -> dict:
    out: dict = {}
    if "num_results" in value:
        out["NumResults"] = value["num_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "qualification_requests" in value:
        import capo_mturk.types.qualification_request_list

        out["QualificationRequests"] = (
            capo_mturk.types.qualification_request_list.serialize_aws_json_1_1(
                value["qualification_requests"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListQualificationRequestsResponse:
    out: ListQualificationRequestsResponse = {}  # type: ignore[typeddict-item]
    if "NumResults" in data:
        out["num_results"] = data["NumResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "QualificationRequests" in data:
        import capo_mturk.types.qualification_request_list

        out["qualification_requests"] = (
            capo_mturk.types.qualification_request_list.deserialize_aws_json_1_1(
                data["QualificationRequests"]
            )
        )
    return out
