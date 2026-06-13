"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#ListOrganizationRecommendationAccountsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_trustedadvisor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_trustedadvisor.types.account_recommendation_lifecycle_summary_list


class ListOrganizationRecommendationAccountsResponse(TypedDict):
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""
    account_recommendation_lifecycle_summaries: "aws_sdk_trustedadvisor.types.account_recommendation_lifecycle_summary_list.AccountRecommendationLifecycleSummaryList"
    """<p>The account recommendations lifecycles that are applicable to the Recommendation</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOrganizationRecommendationAccountsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_trustedadvisor.types.account_recommendation_lifecycle_summary_list

    out["accountRecommendationLifecycleSummaries"] = (
        aws_sdk_trustedadvisor.types.account_recommendation_lifecycle_summary_list.serialize_json(
            value["account_recommendation_lifecycle_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListOrganizationRecommendationAccountsResponse:
    out: ListOrganizationRecommendationAccountsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "accountRecommendationLifecycleSummaries" in data:
        import aws_sdk_trustedadvisor.types.account_recommendation_lifecycle_summary_list

        out["account_recommendation_lifecycle_summaries"] = (
            aws_sdk_trustedadvisor.types.account_recommendation_lifecycle_summary_list.deserialize_json(
                data["accountRecommendationLifecycleSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListOrganizationRecommendationAccountsResponse.account_recommendation_lifecycle_summaries required"
        )
    return out
