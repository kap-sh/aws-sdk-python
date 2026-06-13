"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateBrandResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.brand_definition
    import aws_sdk_quicksight.types.brand_detail
    import aws_sdk_quicksight.types.string


class CreateBrandResponse(TypedDict):
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    brand_detail: NotRequired["aws_sdk_quicksight.types.brand_detail.BrandDetail"]
    """<p>The details of the brand.</p>"""
    brand_definition: NotRequired[
        "aws_sdk_quicksight.types.brand_definition.BrandDefinition"
    ]
    """<p>The definition of the brand.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBrandResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "brand_detail" in value:
        import aws_sdk_quicksight.types.brand_detail

        out["BrandDetail"] = aws_sdk_quicksight.types.brand_detail.serialize_json(
            value["brand_detail"]
        )
    if "brand_definition" in value:
        import aws_sdk_quicksight.types.brand_definition

        out["BrandDefinition"] = (
            aws_sdk_quicksight.types.brand_definition.serialize_json(
                value["brand_definition"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateBrandResponse:
    out: CreateBrandResponse = {}  # type: ignore[typeddict-item]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "BrandDetail" in data:
        import aws_sdk_quicksight.types.brand_detail

        out["brand_detail"] = aws_sdk_quicksight.types.brand_detail.deserialize_json(
            data["BrandDetail"]
        )
    if "BrandDefinition" in data:
        import aws_sdk_quicksight.types.brand_definition

        out["brand_definition"] = (
            aws_sdk_quicksight.types.brand_definition.deserialize_json(
                data["BrandDefinition"]
            )
        )
    return out
