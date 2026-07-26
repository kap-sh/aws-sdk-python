"""Generated from Smithy shape ``com.amazonaws.licensemanager#ProductInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_license_manager.types.product_information

ProductInformationList: TypeAlias = list[
    "capo_license_manager.types.product_information.ProductInformation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductInformationList) -> list:
    import capo_license_manager.types.product_information

    out: list = []
    for item in value:
        out.append(
            capo_license_manager.types.product_information.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProductInformationList:
    import capo_license_manager.types.product_information

    out: ProductInformationList = []
    for item in data:
        out.append(
            capo_license_manager.types.product_information.deserialize_aws_json_1_1(
                item
            )
        )
    return out
