"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#DataProductEntityIdFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.data_product_entity_id_filter_value_list


class DataProductEntityIdFilter(TypedDict, closed=True):
    value_list: NotRequired[
        "capo_marketplace_catalog.types.data_product_entity_id_filter_value_list.DataProductEntityIdFilterValueList"
    ]
    """<p>A string array of unique entity id values to be filtered on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataProductEntityIdFilter) -> dict:
    out: dict = {}
    if "value_list" in value:
        import capo_marketplace_catalog.types.data_product_entity_id_filter_value_list

        out["ValueList"] = (
            capo_marketplace_catalog.types.data_product_entity_id_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataProductEntityIdFilter:
    out: DataProductEntityIdFilter = {}  # type: ignore[typeddict-item]
    if "ValueList" in data:
        import capo_marketplace_catalog.types.data_product_entity_id_filter_value_list

        out["value_list"] = (
            capo_marketplace_catalog.types.data_product_entity_id_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    return out
