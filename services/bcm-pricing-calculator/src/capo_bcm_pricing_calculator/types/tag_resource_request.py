"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.arn
    import capo_bcm_pricing_calculator.types.tags


class TagResourceRequest(TypedDict, closed=True):
    arn: "capo_bcm_pricing_calculator.types.arn.Arn"
    """<p> The Amazon Resource Name (ARN) of the resource to add tags to. </p>"""
    tags: "capo_bcm_pricing_calculator.types.tags.Tags"
    """<p> The tags to add to the resource. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import capo_bcm_pricing_calculator.types.tags

    out["tags"] = capo_bcm_pricing_calculator.types.tags.serialize_aws_json_1_0(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("TagResourceRequest.arn required")
    if "tags" in data:
        import capo_bcm_pricing_calculator.types.tags

        out["tags"] = capo_bcm_pricing_calculator.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
