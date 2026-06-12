"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#EntityDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.entity_detail
    import aws_sdk_marketplace_catalog.types.entity_id

EntityDetails: TypeAlias = dict[
    "aws_sdk_marketplace_catalog.types.entity_id.EntityId",
    "aws_sdk_marketplace_catalog.types.entity_detail.EntityDetail",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: EntityDetails) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_marketplace_catalog.types.entity_detail

        out[key] = aws_sdk_marketplace_catalog.types.entity_detail.serialize_json(value)
    return out


def deserialize_json(data: dict) -> EntityDetails:
    out: EntityDetails = {}
    for key, value in data.items():
        import aws_sdk_marketplace_catalog.types.entity_detail

        out[key] = aws_sdk_marketplace_catalog.types.entity_detail.deserialize_json(
            value
        )
    return out
