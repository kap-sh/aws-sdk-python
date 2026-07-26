"""Generated from Smithy shape ``com.amazonaws.licensemanager#ProductInformationFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager.types.string
    import capo_license_manager.types.string_list


class ProductInformationFilter(TypedDict, closed=True):
    product_information_filter_name: "capo_license_manager.types.string.String"
    """<p>Filter name.</p>"""
    product_information_filter_value: NotRequired[
        "capo_license_manager.types.string_list.StringList"
    ]
    """<p>Filter value.</p>"""
    product_information_filter_comparator: "capo_license_manager.types.string.String"
    """<p>Logical operator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductInformationFilter) -> dict:
    out: dict = {}
    out["ProductInformationFilterName"] = value["product_information_filter_name"]
    if "product_information_filter_value" in value:
        import capo_license_manager.types.string_list

        out["ProductInformationFilterValue"] = (
            capo_license_manager.types.string_list.serialize_aws_json_1_1(
                value["product_information_filter_value"]
            )
        )
    out["ProductInformationFilterComparator"] = value[
        "product_information_filter_comparator"
    ]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProductInformationFilter:
    out: ProductInformationFilter = {}  # type: ignore[typeddict-item]
    if "ProductInformationFilterName" in data:
        out["product_information_filter_name"] = data["ProductInformationFilterName"]
    else:
        raise DeserializationError(
            "ProductInformationFilter.product_information_filter_name required"
        )
    if "ProductInformationFilterValue" in data:
        import capo_license_manager.types.string_list

        out["product_information_filter_value"] = (
            capo_license_manager.types.string_list.deserialize_aws_json_1_1(
                data["ProductInformationFilterValue"]
            )
        )
    if "ProductInformationFilterComparator" in data:
        out["product_information_filter_comparator"] = data[
            "ProductInformationFilterComparator"
        ]
    else:
        raise DeserializationError(
            "ProductInformationFilter.product_information_filter_comparator required"
        )
    return out
