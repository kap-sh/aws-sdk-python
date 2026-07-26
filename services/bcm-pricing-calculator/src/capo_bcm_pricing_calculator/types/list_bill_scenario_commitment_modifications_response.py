"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListBillScenarioCommitmentModificationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.bill_scenario_commitment_modification_items
    import capo_bcm_pricing_calculator.types.next_page_token


class ListBillScenarioCommitmentModificationsResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_bcm_pricing_calculator.types.bill_scenario_commitment_modification_items.BillScenarioCommitmentModificationItems"
    ]
    """<p> The list of commitment modifications associated with the bill scenario. </p>"""
    next_token: NotRequired[
        "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
    ]
    """<p> A token to retrieve the next page of results, if any. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ListBillScenarioCommitmentModificationsResponse,
) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_bcm_pricing_calculator.types.bill_scenario_commitment_modification_items

        out["items"] = (
            capo_bcm_pricing_calculator.types.bill_scenario_commitment_modification_items.serialize_aws_json_1_0(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ListBillScenarioCommitmentModificationsResponse:
    out: ListBillScenarioCommitmentModificationsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_bcm_pricing_calculator.types.bill_scenario_commitment_modification_items

        out["items"] = (
            capo_bcm_pricing_calculator.types.bill_scenario_commitment_modification_items.deserialize_aws_json_1_0(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
