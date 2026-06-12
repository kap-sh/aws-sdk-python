"""Generated from Smithy shape ``com.amazonaws.licensemanager#ProductCodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.product_code_list_item

ProductCodeList: TypeAlias = list[
    "aws_sdk_license_manager.types.product_code_list_item.ProductCodeListItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductCodeList) -> list:
    import aws_sdk_license_manager.types.product_code_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_license_manager.types.product_code_list_item.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProductCodeList:
    import aws_sdk_license_manager.types.product_code_list_item

    out: ProductCodeList = []
    for item in data:
        out.append(
            aws_sdk_license_manager.types.product_code_list_item.deserialize_aws_json_1_1(
                item
            )
        )
    return out
