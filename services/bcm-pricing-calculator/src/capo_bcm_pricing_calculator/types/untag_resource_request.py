"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.arn
    import capo_bcm_pricing_calculator.types.resource_tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    arn: "capo_bcm_pricing_calculator.types.arn.Arn"
    """<p> The Amazon Resource Name (ARN) of the resource to remove tags from. </p>"""
    tag_keys: "capo_bcm_pricing_calculator.types.resource_tag_keys.ResourceTagKeys"
    """<p> The keys of the tags to remove from the resource. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import capo_bcm_pricing_calculator.types.resource_tag_keys

    out["tagKeys"] = (
        capo_bcm_pricing_calculator.types.resource_tag_keys.serialize_aws_json_1_0(
            value["tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UntagResourceRequest.arn required")
    if "tagKeys" in data:
        import capo_bcm_pricing_calculator.types.resource_tag_keys

        out["tag_keys"] = (
            capo_bcm_pricing_calculator.types.resource_tag_keys.deserialize_aws_json_1_0(
                data["tagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
