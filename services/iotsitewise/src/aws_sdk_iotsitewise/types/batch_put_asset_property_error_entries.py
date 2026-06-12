"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchPutAssetPropertyErrorEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.batch_put_asset_property_error_entry

BatchPutAssetPropertyErrorEntries: TypeAlias = list[
    "aws_sdk_iotsitewise.types.batch_put_asset_property_error_entry.BatchPutAssetPropertyErrorEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutAssetPropertyErrorEntries) -> list:
    import aws_sdk_iotsitewise.types.batch_put_asset_property_error_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotsitewise.types.batch_put_asset_property_error_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchPutAssetPropertyErrorEntries:
    import aws_sdk_iotsitewise.types.batch_put_asset_property_error_entry

    out: BatchPutAssetPropertyErrorEntries = []
    for item in data:
        out.append(
            aws_sdk_iotsitewise.types.batch_put_asset_property_error_entry.deserialize_json(
                item
            )
        )
    return out
