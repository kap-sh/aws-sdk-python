"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotS3DestinationConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.snapshot_s3_destination_configuration

SnapshotS3DestinationConfigurationList: TypeAlias = list[
    "capo_quicksight.types.snapshot_s3_destination_configuration.SnapshotS3DestinationConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotS3DestinationConfigurationList) -> list:
    import capo_quicksight.types.snapshot_s3_destination_configuration

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.snapshot_s3_destination_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SnapshotS3DestinationConfigurationList:
    import capo_quicksight.types.snapshot_s3_destination_configuration

    out: SnapshotS3DestinationConfigurationList = []
    for item in data:
        out.append(
            capo_quicksight.types.snapshot_s3_destination_configuration.deserialize_json(
                item
            )
        )
    return out
