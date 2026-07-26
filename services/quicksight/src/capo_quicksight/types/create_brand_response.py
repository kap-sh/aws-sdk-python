"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateBrandResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.brand_definition
    import capo_quicksight.types.brand_detail
    import capo_quicksight.types.string


class CreateBrandResponse(TypedDict, closed=True):
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    brand_detail: NotRequired["capo_quicksight.types.brand_detail.BrandDetail"]
    """<p>The details of the brand.</p>"""
    brand_definition: NotRequired[
        "capo_quicksight.types.brand_definition.BrandDefinition"
    ]
    """<p>The definition of the brand.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBrandResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "brand_detail" in value:
        import capo_quicksight.types.brand_detail

        out["BrandDetail"] = capo_quicksight.types.brand_detail.serialize_json(
            value["brand_detail"]
        )
    if "brand_definition" in value:
        import capo_quicksight.types.brand_definition

        out["BrandDefinition"] = capo_quicksight.types.brand_definition.serialize_json(
            value["brand_definition"]
        )
    return out


def deserialize_json(data: dict) -> CreateBrandResponse:
    out: CreateBrandResponse = {}  # type: ignore[typeddict-item]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "BrandDetail" in data:
        import capo_quicksight.types.brand_detail

        out["brand_detail"] = capo_quicksight.types.brand_detail.deserialize_json(
            data["BrandDetail"]
        )
    if "BrandDefinition" in data:
        import capo_quicksight.types.brand_definition

        out["brand_definition"] = (
            capo_quicksight.types.brand_definition.deserialize_json(
                data["BrandDefinition"]
            )
        )
    return out
