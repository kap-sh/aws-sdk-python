"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.tags


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_bcm_pricing_calculator.types.tags.Tags"]
    """<p> The list of tags associated with the specified resource. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_bcm_pricing_calculator.types.tags

        out["tags"] = aws_sdk_bcm_pricing_calculator.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_bcm_pricing_calculator.types.tags

        out["tags"] = (
            aws_sdk_bcm_pricing_calculator.types.tags.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    return out
