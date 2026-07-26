"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#AmiProductVisibilityFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.ami_product_visibility_filter_value_list


class AmiProductVisibilityFilter(TypedDict, closed=True):
    value_list: NotRequired[
        "capo_marketplace_catalog.types.ami_product_visibility_filter_value_list.AmiProductVisibilityFilterValueList"
    ]
    """<p>A string array of unique visibility values to be filtered on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmiProductVisibilityFilter) -> dict:
    out: dict = {}
    if "value_list" in value:
        import capo_marketplace_catalog.types.ami_product_visibility_filter_value_list

        out["ValueList"] = (
            capo_marketplace_catalog.types.ami_product_visibility_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> AmiProductVisibilityFilter:
    out: AmiProductVisibilityFilter = {}  # type: ignore[typeddict-item]
    if "ValueList" in data:
        import capo_marketplace_catalog.types.ami_product_visibility_filter_value_list

        out["value_list"] = (
            capo_marketplace_catalog.types.ami_product_visibility_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    return out
