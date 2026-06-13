"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#DeleteBillEstimateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.resource_id


class DeleteBillEstimateRequest(TypedDict):
    identifier: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The unique identifier of the bill estimate to delete. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteBillEstimateRequest) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteBillEstimateRequest:
    out: DeleteBillEstimateRequest = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("DeleteBillEstimateRequest.identifier required")
    return out
