"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#EntitySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.entity_summary

EntitySummaryList: TypeAlias = list[
    "capo_marketplace_catalog.types.entity_summary.EntitySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EntitySummaryList) -> list:
    import capo_marketplace_catalog.types.entity_summary

    out: list = []
    for item in value:
        out.append(capo_marketplace_catalog.types.entity_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> EntitySummaryList:
    import capo_marketplace_catalog.types.entity_summary

    out: EntitySummaryList = []
    for item in data:
        out.append(capo_marketplace_catalog.types.entity_summary.deserialize_json(item))
    return out
