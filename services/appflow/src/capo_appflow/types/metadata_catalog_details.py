"""Generated from Smithy shape ``com.amazonaws.appflow#MetadataCatalogDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.metadata_catalog_detail

MetadataCatalogDetails: TypeAlias = list[
    "capo_appflow.types.metadata_catalog_detail.MetadataCatalogDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetadataCatalogDetails) -> list:
    import capo_appflow.types.metadata_catalog_detail

    out: list = []
    for item in value:
        out.append(capo_appflow.types.metadata_catalog_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetadataCatalogDetails:
    import capo_appflow.types.metadata_catalog_detail

    out: MetadataCatalogDetails = []
    for item in data:
        out.append(capo_appflow.types.metadata_catalog_detail.deserialize_json(item))
    return out
