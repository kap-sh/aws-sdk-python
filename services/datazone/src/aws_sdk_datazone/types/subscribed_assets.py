"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedAssets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.subscribed_asset

SubscribedAssets: TypeAlias = list[
    "aws_sdk_datazone.types.subscribed_asset.SubscribedAsset"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedAssets) -> list:
    import aws_sdk_datazone.types.subscribed_asset

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.subscribed_asset.serialize_json(item))
    return out


def deserialize_json(data: list) -> SubscribedAssets:
    import aws_sdk_datazone.types.subscribed_asset

    out: SubscribedAssets = []
    for item in data:
        out.append(aws_sdk_datazone.types.subscribed_asset.deserialize_json(item))
    return out
