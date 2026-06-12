"""Generated from Smithy shape ``com.amazonaws.savingsplans#DescribeSavingsPlansRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.max_results
    import aws_sdk_savingsplans.types.pagination_token
    import aws_sdk_savingsplans.types.savings_plan_arn_list
    import aws_sdk_savingsplans.types.savings_plan_filter_list
    import aws_sdk_savingsplans.types.savings_plan_id_list
    import aws_sdk_savingsplans.types.savings_plan_state_list


class DescribeSavingsPlansRequest(TypedDict):
    savings_plan_arns: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_arn_list.SavingsPlanArnList"
    ]
    """<p>The Amazon Resource Names (ARN) of the Savings Plans.</p>"""
    savings_plan_ids: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_id_list.SavingsPlanIdList"
    ]
    """<p>The IDs of the Savings Plans.</p>"""
    next_token: NotRequired[
        "aws_sdk_savingsplans.types.pagination_token.PaginationToken"
    ]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_savingsplans.types.max_results.MaxResults"]
    """<p>The maximum number of results to return with a single call. To retrieve additional results, make another call with the returned token value.</p>"""
    states: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_state_list.SavingsPlanStateList"
    ]
    """<p>The current states of the Savings Plans.</p>"""
    filters: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_filter_list.SavingsPlanFilterList"
    ]
    """<p>The filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSavingsPlansRequest) -> dict:
    out: dict = {}
    if "savings_plan_arns" in value:
        import aws_sdk_savingsplans.types.savings_plan_arn_list

        out["savingsPlanArns"] = (
            aws_sdk_savingsplans.types.savings_plan_arn_list.serialize_json(
                value["savings_plan_arns"]
            )
        )
    if "savings_plan_ids" in value:
        import aws_sdk_savingsplans.types.savings_plan_id_list

        out["savingsPlanIds"] = (
            aws_sdk_savingsplans.types.savings_plan_id_list.serialize_json(
                value["savings_plan_ids"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "states" in value:
        import aws_sdk_savingsplans.types.savings_plan_state_list

        out["states"] = (
            aws_sdk_savingsplans.types.savings_plan_state_list.serialize_json(
                value["states"]
            )
        )
    if "filters" in value:
        import aws_sdk_savingsplans.types.savings_plan_filter_list

        out["filters"] = (
            aws_sdk_savingsplans.types.savings_plan_filter_list.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeSavingsPlansRequest:
    out: DescribeSavingsPlansRequest = {}  # type: ignore[typeddict-item]
    if "savingsPlanArns" in data:
        import aws_sdk_savingsplans.types.savings_plan_arn_list

        out["savings_plan_arns"] = (
            aws_sdk_savingsplans.types.savings_plan_arn_list.deserialize_json(
                data["savingsPlanArns"]
            )
        )
    if "savingsPlanIds" in data:
        import aws_sdk_savingsplans.types.savings_plan_id_list

        out["savings_plan_ids"] = (
            aws_sdk_savingsplans.types.savings_plan_id_list.deserialize_json(
                data["savingsPlanIds"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "states" in data:
        import aws_sdk_savingsplans.types.savings_plan_state_list

        out["states"] = (
            aws_sdk_savingsplans.types.savings_plan_state_list.deserialize_json(
                data["states"]
            )
        )
    if "filters" in data:
        import aws_sdk_savingsplans.types.savings_plan_filter_list

        out["filters"] = (
            aws_sdk_savingsplans.types.savings_plan_filter_list.deserialize_json(
                data["filters"]
            )
        )
    return out
