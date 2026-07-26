"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SaaSProductVisibilityFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.saa_s_product_visibility_filter_value_list


class SaaSProductVisibilityFilter(TypedDict, closed=True):
    value_list: NotRequired[
        "capo_marketplace_catalog.types.saa_s_product_visibility_filter_value_list.SaaSProductVisibilityFilterValueList"
    ]
    """<p>A string array of unique visibility values to be filtered on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SaaSProductVisibilityFilter) -> dict:
    out: dict = {}
    if "value_list" in value:
        import capo_marketplace_catalog.types.saa_s_product_visibility_filter_value_list

        out["ValueList"] = (
            capo_marketplace_catalog.types.saa_s_product_visibility_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> SaaSProductVisibilityFilter:
    out: SaaSProductVisibilityFilter = {}  # type: ignore[typeddict-item]
    if "ValueList" in data:
        import capo_marketplace_catalog.types.saa_s_product_visibility_filter_value_list

        out["value_list"] = (
            capo_marketplace_catalog.types.saa_s_product_visibility_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    return out
