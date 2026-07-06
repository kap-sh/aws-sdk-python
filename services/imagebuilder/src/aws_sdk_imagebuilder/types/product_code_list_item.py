"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ProductCodeListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.product_code_id
    import aws_sdk_imagebuilder.types.product_code_type


class ProductCodeListItem(TypedDict, closed=True):
    product_code_id: "aws_sdk_imagebuilder.types.product_code_id.ProductCodeId"
    """<p>For Amazon Web Services Marketplace components, this contains the product code ID that can be stamped onto an EC2 AMI to ensure that components are billed correctly. If this property is empty, it might mean that the component is not published.</p>"""
    product_code_type: "aws_sdk_imagebuilder.types.product_code_type.ProductCodeType"
    """<p>The owner of the product code that's billed. If this property is empty, it might mean that the component is not published.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProductCodeListItem) -> dict:
    out: dict = {}
    out["productCodeId"] = value["product_code_id"]
    import aws_sdk_imagebuilder.types.product_code_type

    out["productCodeType"] = (
        aws_sdk_imagebuilder.types.product_code_type.serialize_json(
            value["product_code_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> ProductCodeListItem:
    out: ProductCodeListItem = {}  # type: ignore[typeddict-item]
    if "productCodeId" in data:
        out["product_code_id"] = data["productCodeId"]
    else:
        raise DeserializationError("ProductCodeListItem.product_code_id required")
    if "productCodeType" in data:
        import aws_sdk_imagebuilder.types.product_code_type

        out["product_code_type"] = (
            aws_sdk_imagebuilder.types.product_code_type.deserialize_json(
                data["productCodeType"]
            )
        )
    else:
        raise DeserializationError("ProductCodeListItem.product_code_type required")
    return out
