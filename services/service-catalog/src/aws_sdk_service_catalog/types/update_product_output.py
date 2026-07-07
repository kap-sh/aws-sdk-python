"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UpdateProductOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.product_view_detail
    import aws_sdk_service_catalog.types.tags


class UpdateProductOutput(TypedDict, closed=True):
    product_view_detail: NotRequired[
        "aws_sdk_service_catalog.types.product_view_detail.ProductViewDetail"
    ]
    """<p>Information about the product view.</p>"""
    tags: NotRequired["aws_sdk_service_catalog.types.tags.Tags"]
    """<p>Information about the tags associated with the product.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProductOutput) -> dict:
    out: dict = {}
    if "product_view_detail" in value:
        import aws_sdk_service_catalog.types.product_view_detail

        out["ProductViewDetail"] = (
            aws_sdk_service_catalog.types.product_view_detail.serialize_aws_json_1_1(
                value["product_view_detail"]
            )
        )
    if "tags" in value:
        import aws_sdk_service_catalog.types.tags

        out["Tags"] = aws_sdk_service_catalog.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProductOutput:
    out: UpdateProductOutput = {}  # type: ignore[typeddict-item]
    if "ProductViewDetail" in data:
        import aws_sdk_service_catalog.types.product_view_detail

        out["product_view_detail"] = (
            aws_sdk_service_catalog.types.product_view_detail.deserialize_aws_json_1_1(
                data["ProductViewDetail"]
            )
        )
    if "Tags" in data:
        import aws_sdk_service_catalog.types.tags

        out["tags"] = aws_sdk_service_catalog.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
