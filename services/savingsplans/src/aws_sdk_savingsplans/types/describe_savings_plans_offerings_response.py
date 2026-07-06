"""Generated from Smithy shape ``com.amazonaws.savingsplans#DescribeSavingsPlansOfferingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.pagination_token
    import aws_sdk_savingsplans.types.savings_plan_offerings_list


class DescribeSavingsPlansOfferingsResponse(TypedDict, closed=True):
    search_results: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_offerings_list.SavingsPlanOfferingsList"
    ]
    """<p>Information about the Savings Plans offerings.</p>"""
    next_token: NotRequired[
        "aws_sdk_savingsplans.types.pagination_token.PaginationToken"
    ]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSavingsPlansOfferingsResponse) -> dict:
    out: dict = {}
    if "search_results" in value:
        import aws_sdk_savingsplans.types.savings_plan_offerings_list

        out["searchResults"] = (
            aws_sdk_savingsplans.types.savings_plan_offerings_list.serialize_json(
                value["search_results"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeSavingsPlansOfferingsResponse:
    out: DescribeSavingsPlansOfferingsResponse = {}  # type: ignore[typeddict-item]
    if "searchResults" in data:
        import aws_sdk_savingsplans.types.savings_plan_offerings_list

        out["search_results"] = (
            aws_sdk_savingsplans.types.savings_plan_offerings_list.deserialize_json(
                data["searchResults"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
