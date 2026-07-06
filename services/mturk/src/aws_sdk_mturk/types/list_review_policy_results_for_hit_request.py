"""Generated from Smithy shape ``com.amazonaws.mturk#ListReviewPolicyResultsForHITRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mturk.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mturk.types.boolean
    import aws_sdk_mturk.types.entity_id
    import aws_sdk_mturk.types.pagination_token
    import aws_sdk_mturk.types.result_size
    import aws_sdk_mturk.types.review_policy_level_list


class ListReviewPolicyResultsForHITRequest(TypedDict, closed=True):
    hit_id: "aws_sdk_mturk.types.entity_id.EntityId"
    """<p>The unique identifier of the HIT to retrieve review results for.</p>"""
    policy_levels: NotRequired[
        "aws_sdk_mturk.types.review_policy_level_list.ReviewPolicyLevelList"
    ]
    """<p> The Policy Level(s) to retrieve review results for - HIT or Assignment. If omitted, the default behavior is to retrieve all data for both policy levels. For a list of all the described policies, see Review Policies. </p>"""
    retrieve_actions: NotRequired["aws_sdk_mturk.types.boolean.Boolean"]
    """<p> Specify if the operation should retrieve a list of the actions taken executing the Review Policies and their outcomes. </p>"""
    retrieve_results: NotRequired["aws_sdk_mturk.types.boolean.Boolean"]
    """<p> Specify if the operation should retrieve a list of the results computed by the Review Policies. </p>"""
    next_token: NotRequired["aws_sdk_mturk.types.pagination_token.PaginationToken"]
    """<p>Pagination token</p>"""
    max_results: NotRequired["aws_sdk_mturk.types.result_size.ResultSize"]
    """<p>Limit the number of results returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListReviewPolicyResultsForHITRequest) -> dict:
    out: dict = {}
    out["HITId"] = value["hit_id"]
    if "policy_levels" in value:
        import aws_sdk_mturk.types.review_policy_level_list

        out["PolicyLevels"] = (
            aws_sdk_mturk.types.review_policy_level_list.serialize_aws_json_1_1(
                value["policy_levels"]
            )
        )
    if "retrieve_actions" in value:
        out["RetrieveActions"] = value["retrieve_actions"]
    if "retrieve_results" in value:
        out["RetrieveResults"] = value["retrieve_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListReviewPolicyResultsForHITRequest:
    out: ListReviewPolicyResultsForHITRequest = {}  # type: ignore[typeddict-item]
    if "HITId" in data:
        out["hit_id"] = data["HITId"]
    else:
        raise DeserializationError(
            "ListReviewPolicyResultsForHITRequest.hit_id required"
        )
    if "PolicyLevels" in data:
        import aws_sdk_mturk.types.review_policy_level_list

        out["policy_levels"] = (
            aws_sdk_mturk.types.review_policy_level_list.deserialize_aws_json_1_1(
                data["PolicyLevels"]
            )
        )
    if "RetrieveActions" in data:
        out["retrieve_actions"] = data["RetrieveActions"]
    if "RetrieveResults" in data:
        out["retrieve_results"] = data["RetrieveResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
