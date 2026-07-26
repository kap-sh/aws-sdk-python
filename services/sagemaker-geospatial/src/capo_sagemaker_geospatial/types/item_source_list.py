"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ItemSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.item_source

ItemSourceList: TypeAlias = list[
    "capo_sagemaker_geospatial.types.item_source.ItemSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: ItemSourceList) -> list:
    import capo_sagemaker_geospatial.types.item_source

    out: list = []
    for item in value:
        out.append(capo_sagemaker_geospatial.types.item_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> ItemSourceList:
    import capo_sagemaker_geospatial.types.item_source

    out: ItemSourceList = []
    for item in data:
        out.append(capo_sagemaker_geospatial.types.item_source.deserialize_json(item))
    return out
