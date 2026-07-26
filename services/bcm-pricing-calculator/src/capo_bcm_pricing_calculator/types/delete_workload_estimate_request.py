"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#DeleteWorkloadEstimateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.resource_id


class DeleteWorkloadEstimateRequest(TypedDict, closed=True):
    identifier: "capo_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The unique identifier of the workload estimate to delete. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteWorkloadEstimateRequest) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteWorkloadEstimateRequest:
    out: DeleteWorkloadEstimateRequest = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("DeleteWorkloadEstimateRequest.identifier required")
    return out
