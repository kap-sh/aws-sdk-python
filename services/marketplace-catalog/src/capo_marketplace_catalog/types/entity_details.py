"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#EntityDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.entity_detail
    import capo_marketplace_catalog.types.entity_id

EntityDetails: TypeAlias = dict[
    "capo_marketplace_catalog.types.entity_id.EntityId",
    "capo_marketplace_catalog.types.entity_detail.EntityDetail",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: EntityDetails) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_marketplace_catalog.types.entity_detail

        out[key] = capo_marketplace_catalog.types.entity_detail.serialize_json(value)
    return out


def deserialize_json(data: dict) -> EntityDetails:
    out: EntityDetails = {}
    for key, value in data.items():
        import capo_marketplace_catalog.types.entity_detail

        out[key] = capo_marketplace_catalog.types.entity_detail.deserialize_json(value)
    return out
