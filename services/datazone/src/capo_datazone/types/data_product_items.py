"""Generated from Smithy shape ``com.amazonaws.datazone#DataProductItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.data_product_item

DataProductItems: TypeAlias = list[
    "capo_datazone.types.data_product_item.DataProductItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataProductItems) -> list:
    import capo_datazone.types.data_product_item

    out: list = []
    for item in value:
        out.append(capo_datazone.types.data_product_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataProductItems:
    import capo_datazone.types.data_product_item

    out: DataProductItems = []
    for item in data:
        out.append(capo_datazone.types.data_product_item.deserialize_json(item))
    return out
