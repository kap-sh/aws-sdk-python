"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#GetWorkloadEstimateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.resource_id


class GetWorkloadEstimateRequest(TypedDict, closed=True):
    identifier: "capo_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The unique identifier of the workload estimate to retrieve. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetWorkloadEstimateRequest) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetWorkloadEstimateRequest:
    out: GetWorkloadEstimateRequest = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("GetWorkloadEstimateRequest.identifier required")
    return out
