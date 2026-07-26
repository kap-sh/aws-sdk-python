"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchAssociateProjectAssetsErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_error_details

BatchAssociateProjectAssetsErrors: TypeAlias = list[
    "capo_iotsitewise.types.asset_error_details.AssetErrorDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchAssociateProjectAssetsErrors) -> list:
    import capo_iotsitewise.types.asset_error_details

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.asset_error_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchAssociateProjectAssetsErrors:
    import capo_iotsitewise.types.asset_error_details

    out: BatchAssociateProjectAssetsErrors = []
    for item in data:
        out.append(capo_iotsitewise.types.asset_error_details.deserialize_json(item))
    return out
