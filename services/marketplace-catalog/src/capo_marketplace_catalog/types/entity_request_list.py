"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#EntityRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.entity_request

EntityRequestList: TypeAlias = list[
    "capo_marketplace_catalog.types.entity_request.EntityRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: EntityRequestList) -> list:
    import capo_marketplace_catalog.types.entity_request

    out: list = []
    for item in value:
        out.append(capo_marketplace_catalog.types.entity_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> EntityRequestList:
    import capo_marketplace_catalog.types.entity_request

    out: EntityRequestList = []
    for item in data:
        out.append(capo_marketplace_catalog.types.entity_request.deserialize_json(item))
    return out
