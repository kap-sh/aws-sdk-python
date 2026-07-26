"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#Errors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.batch_describe_error_detail
    import capo_marketplace_catalog.types.entity_id

Errors: TypeAlias = dict[
    "capo_marketplace_catalog.types.entity_id.EntityId",
    "capo_marketplace_catalog.types.batch_describe_error_detail.BatchDescribeErrorDetail",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Errors) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_marketplace_catalog.types.batch_describe_error_detail

        out[key] = (
            capo_marketplace_catalog.types.batch_describe_error_detail.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> Errors:
    out: Errors = {}
    for key, value in data.items():
        import capo_marketplace_catalog.types.batch_describe_error_detail

        out[key] = (
            capo_marketplace_catalog.types.batch_describe_error_detail.deserialize_json(
                value
            )
        )
    return out
