"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#Errors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.batch_describe_error_detail
    import aws_sdk_marketplace_catalog.types.entity_id

Errors: TypeAlias = dict[
    "aws_sdk_marketplace_catalog.types.entity_id.EntityId",
    "aws_sdk_marketplace_catalog.types.batch_describe_error_detail.BatchDescribeErrorDetail",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Errors) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_marketplace_catalog.types.batch_describe_error_detail

        out[key] = (
            aws_sdk_marketplace_catalog.types.batch_describe_error_detail.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> Errors:
    out: Errors = {}
    for key, value in data.items():
        import aws_sdk_marketplace_catalog.types.batch_describe_error_detail

        out[key] = (
            aws_sdk_marketplace_catalog.types.batch_describe_error_detail.deserialize_json(
                value
            )
        )
    return out
