"""Generated from Smithy shape ``com.amazonaws.braket#SearchSpendingLimitsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_braket.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_braket.types.spending_limit_summary_list


class SearchSpendingLimitsResponse(TypedDict, closed=True):
    spending_limits: (
        "aws_sdk_braket.types.spending_limit_summary_list.SpendingLimitSummaryList"
    )
    """<p>An array of spending limit summaries that match the specified filters.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchSpendingLimitsResponse) -> dict:
    out: dict = {}
    import aws_sdk_braket.types.spending_limit_summary_list

    out["spendingLimits"] = (
        aws_sdk_braket.types.spending_limit_summary_list.serialize_json(
            value["spending_limits"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchSpendingLimitsResponse:
    out: SearchSpendingLimitsResponse = {}  # type: ignore[typeddict-item]
    if "spendingLimits" in data:
        import aws_sdk_braket.types.spending_limit_summary_list

        out["spending_limits"] = (
            aws_sdk_braket.types.spending_limit_summary_list.deserialize_json(
                data["spendingLimits"]
            )
        )
    else:
        raise DeserializationError(
            "SearchSpendingLimitsResponse.spending_limits required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
