"""Generated from Smithy shape ``com.amazonaws.mturk#ListReviewableHITsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.entity_id
    import capo_mturk.types.pagination_token
    import capo_mturk.types.result_size
    import capo_mturk.types.reviewable_hit_status


class ListReviewableHITsRequest(TypedDict, closed=True):
    hit_type_id: NotRequired["capo_mturk.types.entity_id.EntityId"]
    """<p> The ID of the HIT type of the HITs to consider for the query. If not specified, all HITs for the Reviewer are considered </p>"""
    status: NotRequired["capo_mturk.types.reviewable_hit_status.ReviewableHITStatus"]
    """<p> Can be either <code>Reviewable</code> or <code>Reviewing</code>. Reviewable is the default value. </p>"""
    next_token: NotRequired["capo_mturk.types.pagination_token.PaginationToken"]
    """<p>Pagination Token</p>"""
    max_results: NotRequired["capo_mturk.types.result_size.ResultSize"]
    """<p> Limit the number of results returned. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListReviewableHITsRequest) -> dict:
    out: dict = {}
    if "hit_type_id" in value:
        out["HITTypeId"] = value["hit_type_id"]
    if "status" in value:
        import capo_mturk.types.reviewable_hit_status

        out["Status"] = capo_mturk.types.reviewable_hit_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListReviewableHITsRequest:
    out: ListReviewableHITsRequest = {}  # type: ignore[typeddict-item]
    if "HITTypeId" in data:
        out["hit_type_id"] = data["HITTypeId"]
    if "Status" in data:
        import capo_mturk.types.reviewable_hit_status

        out["status"] = capo_mturk.types.reviewable_hit_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
