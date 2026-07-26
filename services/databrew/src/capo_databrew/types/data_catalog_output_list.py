"""Generated from Smithy shape ``com.amazonaws.databrew#DataCatalogOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_databrew.types.data_catalog_output

DataCatalogOutputList: TypeAlias = list[
    "capo_databrew.types.data_catalog_output.DataCatalogOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataCatalogOutputList) -> list:
    import capo_databrew.types.data_catalog_output

    out: list = []
    for item in value:
        out.append(capo_databrew.types.data_catalog_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataCatalogOutputList:
    import capo_databrew.types.data_catalog_output

    out: DataCatalogOutputList = []
    for item in data:
        out.append(capo_databrew.types.data_catalog_output.deserialize_json(item))
    return out
