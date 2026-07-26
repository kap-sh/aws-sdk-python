"""Generated from Smithy shape ``com.amazonaws.lightsail#CostEstimates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.cost_estimate

CostEstimates: TypeAlias = list["capo_lightsail.types.cost_estimate.CostEstimate"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostEstimates) -> list:
    import capo_lightsail.types.cost_estimate

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.cost_estimate.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CostEstimates:
    import capo_lightsail.types.cost_estimate

    out: CostEstimates = []
    for item in data:
        out.append(capo_lightsail.types.cost_estimate.deserialize_aws_json_1_1(item))
    return out
