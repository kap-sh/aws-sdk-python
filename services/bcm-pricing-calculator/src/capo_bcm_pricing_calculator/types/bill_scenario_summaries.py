"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BillScenarioSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.bill_scenario_summary

BillScenarioSummaries: TypeAlias = list[
    "capo_bcm_pricing_calculator.types.bill_scenario_summary.BillScenarioSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillScenarioSummaries) -> list:
    import capo_bcm_pricing_calculator.types.bill_scenario_summary

    out: list = []
    for item in value:
        out.append(
            capo_bcm_pricing_calculator.types.bill_scenario_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BillScenarioSummaries:
    import capo_bcm_pricing_calculator.types.bill_scenario_summary

    out: BillScenarioSummaries = []
    for item in data:
        out.append(
            capo_bcm_pricing_calculator.types.bill_scenario_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
