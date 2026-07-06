"""Generated from Smithy shape ``com.amazonaws.savingsplans#DescribeSavingsPlansResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.pagination_token
    import aws_sdk_savingsplans.types.savings_plan_list


class DescribeSavingsPlansResponse(TypedDict, closed=True):
    savings_plans: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_list.SavingsPlanList"
    ]
    """<p>Information about the Savings Plans.</p>"""
    next_token: NotRequired[
        "aws_sdk_savingsplans.types.pagination_token.PaginationToken"
    ]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSavingsPlansResponse) -> dict:
    out: dict = {}
    if "savings_plans" in value:
        import aws_sdk_savingsplans.types.savings_plan_list

        out["savingsPlans"] = (
            aws_sdk_savingsplans.types.savings_plan_list.serialize_json(
                value["savings_plans"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeSavingsPlansResponse:
    out: DescribeSavingsPlansResponse = {}  # type: ignore[typeddict-item]
    if "savingsPlans" in data:
        import aws_sdk_savingsplans.types.savings_plan_list

        out["savings_plans"] = (
            aws_sdk_savingsplans.types.savings_plan_list.deserialize_json(
                data["savingsPlans"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
