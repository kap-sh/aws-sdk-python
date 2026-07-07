"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    arn: "aws_sdk_bcm_pricing_calculator.types.arn.Arn"
    """<p> The Amazon Resource Name (ARN) of the resource to list tags for. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ListTagsForResourceRequest.arn required")
    return out
