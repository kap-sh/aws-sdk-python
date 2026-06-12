"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ContainerProductVisibilityFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.container_product_visibility_filter_value_list


class ContainerProductVisibilityFilter(TypedDict):
    value_list: NotRequired[
        "aws_sdk_marketplace_catalog.types.container_product_visibility_filter_value_list.ContainerProductVisibilityFilterValueList"
    ]
    """<p>A string array of unique visibility values to be filtered on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerProductVisibilityFilter) -> dict:
    out: dict = {}
    if "value_list" in value:
        import aws_sdk_marketplace_catalog.types.container_product_visibility_filter_value_list

        out["ValueList"] = (
            aws_sdk_marketplace_catalog.types.container_product_visibility_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContainerProductVisibilityFilter:
    out: ContainerProductVisibilityFilter = {}  # type: ignore[typeddict-item]
    if "ValueList" in data:
        import aws_sdk_marketplace_catalog.types.container_product_visibility_filter_value_list

        out["value_list"] = (
            aws_sdk_marketplace_catalog.types.container_product_visibility_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    return out
