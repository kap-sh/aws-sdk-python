"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#RequestedChangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.change

RequestedChangeList: TypeAlias = list["capo_marketplace_catalog.types.change.Change"]


# --- restJson1 ser/de ---
def serialize_json(value: RequestedChangeList) -> list:
    import capo_marketplace_catalog.types.change

    out: list = []
    for item in value:
        out.append(capo_marketplace_catalog.types.change.serialize_json(item))
    return out


def deserialize_json(data: list) -> RequestedChangeList:
    import capo_marketplace_catalog.types.change

    out: RequestedChangeList = []
    for item in data:
        out.append(capo_marketplace_catalog.types.change.deserialize_json(item))
    return out
