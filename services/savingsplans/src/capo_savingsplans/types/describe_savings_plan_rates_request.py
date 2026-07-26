"""Generated from Smithy shape ``com.amazonaws.savingsplans#DescribeSavingsPlanRatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_savingsplans.errors import DeserializationError

if TYPE_CHECKING:
    import capo_savingsplans.types.max_results
    import capo_savingsplans.types.pagination_token
    import capo_savingsplans.types.savings_plan_id
    import capo_savingsplans.types.savings_plan_rate_filter_list


class DescribeSavingsPlanRatesRequest(TypedDict, closed=True):
    savings_plan_id: "capo_savingsplans.types.savings_plan_id.SavingsPlanId"
    """<p>The ID of the Savings Plan.</p>"""
    filters: NotRequired[
        "capo_savingsplans.types.savings_plan_rate_filter_list.SavingsPlanRateFilterList"
    ]
    """<p>The filters.</p>"""
    next_token: NotRequired["capo_savingsplans.types.pagination_token.PaginationToken"]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired["capo_savingsplans.types.max_results.MaxResults"]
    """<p>The maximum number of results to return with a single call. To retrieve additional results, make another call with the returned token value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSavingsPlanRatesRequest) -> dict:
    out: dict = {}
    out["savingsPlanId"] = value["savings_plan_id"]
    if "filters" in value:
        import capo_savingsplans.types.savings_plan_rate_filter_list

        out["filters"] = (
            capo_savingsplans.types.savings_plan_rate_filter_list.serialize_json(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> DescribeSavingsPlanRatesRequest:
    out: DescribeSavingsPlanRatesRequest = {}  # type: ignore[typeddict-item]
    if "savingsPlanId" in data:
        out["savings_plan_id"] = data["savingsPlanId"]
    else:
        raise DeserializationError(
            "DescribeSavingsPlanRatesRequest.savings_plan_id required"
        )
    if "filters" in data:
        import capo_savingsplans.types.savings_plan_rate_filter_list

        out["filters"] = (
            capo_savingsplans.types.savings_plan_rate_filter_list.deserialize_json(
                data["filters"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
