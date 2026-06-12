"""Generated from Smithy shape ``com.amazonaws.savingsplans#DescribeSavingsPlanRatesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.pagination_token
    import aws_sdk_savingsplans.types.savings_plan_id
    import aws_sdk_savingsplans.types.savings_plan_rate_list


class DescribeSavingsPlanRatesResponse(TypedDict):
    savings_plan_id: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_id.SavingsPlanId"
    ]
    """<p>The ID of the Savings Plan.</p>"""
    search_results: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_rate_list.SavingsPlanRateList"
    ]
    """<p>Information about the Savings Plan rates.</p>"""
    next_token: NotRequired[
        "aws_sdk_savingsplans.types.pagination_token.PaginationToken"
    ]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSavingsPlanRatesResponse) -> dict:
    out: dict = {}
    if "savings_plan_id" in value:
        out["savingsPlanId"] = value["savings_plan_id"]
    if "search_results" in value:
        import aws_sdk_savingsplans.types.savings_plan_rate_list

        out["searchResults"] = (
            aws_sdk_savingsplans.types.savings_plan_rate_list.serialize_json(
                value["search_results"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeSavingsPlanRatesResponse:
    out: DescribeSavingsPlanRatesResponse = {}  # type: ignore[typeddict-item]
    if "savingsPlanId" in data:
        out["savings_plan_id"] = data["savingsPlanId"]
    if "searchResults" in data:
        import aws_sdk_savingsplans.types.savings_plan_rate_list

        out["search_results"] = (
            aws_sdk_savingsplans.types.savings_plan_rate_list.deserialize_json(
                data["searchResults"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
