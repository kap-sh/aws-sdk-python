"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListBillScenarioUsageModificationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.bill_scenario_usage_modification_items
    import aws_sdk_bcm_pricing_calculator.types.next_page_token


class ListBillScenarioUsageModificationsResponse(TypedDict, closed=True):
    items: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.bill_scenario_usage_modification_items.BillScenarioUsageModificationItems"
    ]
    """<p> The list of usage modifications associated with the bill scenario. </p>"""
    next_token: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.next_page_token.NextPageToken"
    ]
    """<p> A token to retrieve the next page of results, if any. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBillScenarioUsageModificationsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_bcm_pricing_calculator.types.bill_scenario_usage_modification_items

        out["items"] = (
            aws_sdk_bcm_pricing_calculator.types.bill_scenario_usage_modification_items.serialize_aws_json_1_0(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListBillScenarioUsageModificationsResponse:
    out: ListBillScenarioUsageModificationsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_bcm_pricing_calculator.types.bill_scenario_usage_modification_items

        out["items"] = (
            aws_sdk_bcm_pricing_calculator.types.bill_scenario_usage_modification_items.deserialize_aws_json_1_0(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
