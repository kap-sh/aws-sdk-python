"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#DeleteBillScenarioRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.resource_id


class DeleteBillScenarioRequest(TypedDict, closed=True):
    identifier: "capo_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The unique identifier of the bill scenario to delete. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteBillScenarioRequest) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteBillScenarioRequest:
    out: DeleteBillScenarioRequest = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("DeleteBillScenarioRequest.identifier required")
    return out
