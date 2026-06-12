"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfAssetDestinationEntry``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.asset_destination_entry

ListOfAssetDestinationEntry: TypeAlias = list[
    "aws_sdk_dataexchange.types.asset_destination_entry.AssetDestinationEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfAssetDestinationEntry) -> list:
    import aws_sdk_dataexchange.types.asset_destination_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_dataexchange.types.asset_destination_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListOfAssetDestinationEntry:
    import aws_sdk_dataexchange.types.asset_destination_entry

    out: ListOfAssetDestinationEntry = []
    for item in data:
        out.append(
            aws_sdk_dataexchange.types.asset_destination_entry.deserialize_json(item)
        )
    return out
