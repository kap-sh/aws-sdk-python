"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#WorkloadEstimateSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.workload_estimate_summary

WorkloadEstimateSummaries: TypeAlias = list[
    "capo_bcm_pricing_calculator.types.workload_estimate_summary.WorkloadEstimateSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkloadEstimateSummaries) -> list:
    import capo_bcm_pricing_calculator.types.workload_estimate_summary

    out: list = []
    for item in value:
        out.append(
            capo_bcm_pricing_calculator.types.workload_estimate_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> WorkloadEstimateSummaries:
    import capo_bcm_pricing_calculator.types.workload_estimate_summary

    out: WorkloadEstimateSummaries = []
    for item in data:
        out.append(
            capo_bcm_pricing_calculator.types.workload_estimate_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
