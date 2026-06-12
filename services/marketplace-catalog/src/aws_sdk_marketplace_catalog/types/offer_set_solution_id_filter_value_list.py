"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferSetSolutionIdFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.offer_set_solution_id_string

OfferSetSolutionIdFilterValueList: TypeAlias = list[
    "aws_sdk_marketplace_catalog.types.offer_set_solution_id_string.OfferSetSolutionIdString"
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferSetSolutionIdFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> OfferSetSolutionIdFilterValueList:
    return list(data)
