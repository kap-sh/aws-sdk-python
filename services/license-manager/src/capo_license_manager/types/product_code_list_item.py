"""Generated from Smithy shape ``com.amazonaws.licensemanager#ProductCodeListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager.types.product_code_id
    import capo_license_manager.types.product_code_type


class ProductCodeListItem(TypedDict, closed=True):
    product_code_id: "capo_license_manager.types.product_code_id.ProductCodeId"
    """<p>The product code ID</p>"""
    product_code_type: "capo_license_manager.types.product_code_type.ProductCodeType"
    """<p>The product code type</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductCodeListItem) -> dict:
    out: dict = {}
    out["ProductCodeId"] = value["product_code_id"]
    import capo_license_manager.types.product_code_type

    out["ProductCodeType"] = (
        capo_license_manager.types.product_code_type.serialize_aws_json_1_1(
            value["product_code_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProductCodeListItem:
    out: ProductCodeListItem = {}  # type: ignore[typeddict-item]
    if "ProductCodeId" in data:
        out["product_code_id"] = data["ProductCodeId"]
    else:
        raise DeserializationError("ProductCodeListItem.product_code_id required")
    if "ProductCodeType" in data:
        import capo_license_manager.types.product_code_type

        out["product_code_type"] = (
            capo_license_manager.types.product_code_type.deserialize_aws_json_1_1(
                data["ProductCodeType"]
            )
        )
    else:
        raise DeserializationError("ProductCodeListItem.product_code_type required")
    return out
