"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetSavingsPlansCoverageResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.next_page_token
    import aws_sdk_cost_explorer.types.savings_plans_coverages


class GetSavingsPlansCoverageResponse(TypedDict):
    savings_plans_coverages: (
        "aws_sdk_cost_explorer.types.savings_plans_coverages.SavingsPlansCoverages"
    )
    """<p>The amount of spend that your Savings Plans covered.</p>"""
    next_token: NotRequired["aws_sdk_cost_explorer.types.next_page_token.NextPageToken"]
    """<p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSavingsPlansCoverageResponse) -> dict:
    out: dict = {}
    import aws_sdk_cost_explorer.types.savings_plans_coverages

    out["SavingsPlansCoverages"] = (
        aws_sdk_cost_explorer.types.savings_plans_coverages.serialize_aws_json_1_1(
            value["savings_plans_coverages"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSavingsPlansCoverageResponse:
    out: GetSavingsPlansCoverageResponse = {}  # type: ignore[typeddict-item]
    if "SavingsPlansCoverages" in data:
        import aws_sdk_cost_explorer.types.savings_plans_coverages

        out["savings_plans_coverages"] = (
            aws_sdk_cost_explorer.types.savings_plans_coverages.deserialize_aws_json_1_1(
                data["SavingsPlansCoverages"]
            )
        )
    else:
        raise DeserializationError(
            "GetSavingsPlansCoverageResponse.savings_plans_coverages required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
