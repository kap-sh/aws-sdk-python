"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchDisassociateProjectAssetsErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_error_details

BatchDisassociateProjectAssetsErrors: TypeAlias = list[
    "aws_sdk_iotsitewise.types.asset_error_details.AssetErrorDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDisassociateProjectAssetsErrors) -> list:
    import aws_sdk_iotsitewise.types.asset_error_details

    out: list = []
    for item in value:
        out.append(aws_sdk_iotsitewise.types.asset_error_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchDisassociateProjectAssetsErrors:
    import aws_sdk_iotsitewise.types.asset_error_details

    out: BatchDisassociateProjectAssetsErrors = []
    for item in data:
        out.append(aws_sdk_iotsitewise.types.asset_error_details.deserialize_json(item))
    return out
