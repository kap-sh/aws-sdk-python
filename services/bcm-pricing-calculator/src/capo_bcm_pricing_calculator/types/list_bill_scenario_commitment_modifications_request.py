"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListBillScenarioCommitmentModificationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.max_results
    import capo_bcm_pricing_calculator.types.next_page_token
    import capo_bcm_pricing_calculator.types.resource_id


class ListBillScenarioCommitmentModificationsRequest(TypedDict, closed=True):
    bill_scenario_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The unique identifier of the bill scenario to list commitment modifications for. </p>"""
    next_token: NotRequired[
        "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
    ]
    """<p> A token to retrieve the next page of results. </p>"""
    max_results: NotRequired["capo_bcm_pricing_calculator.types.max_results.MaxResults"]
    """<p> The maximum number of results to return per page. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ListBillScenarioCommitmentModificationsRequest,
) -> dict:
    out: dict = {}
    out["billScenarioId"] = value["bill_scenario_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ListBillScenarioCommitmentModificationsRequest:
    out: ListBillScenarioCommitmentModificationsRequest = {}  # type: ignore[typeddict-item]
    if "billScenarioId" in data:
        out["bill_scenario_id"] = data["billScenarioId"]
    else:
        raise DeserializationError(
            "ListBillScenarioCommitmentModificationsRequest.bill_scenario_id required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
