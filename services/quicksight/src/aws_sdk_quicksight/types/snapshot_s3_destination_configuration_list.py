"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotS3DestinationConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.snapshot_s3_destination_configuration

SnapshotS3DestinationConfigurationList: TypeAlias = list[
    "aws_sdk_quicksight.types.snapshot_s3_destination_configuration.SnapshotS3DestinationConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotS3DestinationConfigurationList) -> list:
    import aws_sdk_quicksight.types.snapshot_s3_destination_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.snapshot_s3_destination_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SnapshotS3DestinationConfigurationList:
    import aws_sdk_quicksight.types.snapshot_s3_destination_configuration

    out: SnapshotS3DestinationConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.snapshot_s3_destination_configuration.deserialize_json(
                item
            )
        )
    return out
