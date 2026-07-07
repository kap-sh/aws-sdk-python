"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotDestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.snapshot_s3_destination_configuration_list


class SnapshotDestinationConfiguration(TypedDict, closed=True):
    s3_destinations: NotRequired[
        "aws_sdk_quicksight.types.snapshot_s3_destination_configuration_list.SnapshotS3DestinationConfigurationList"
    ]
    """<p> A list of <code>SnapshotS3DestinationConfiguration</code> objects that contain Amazon S3 destination configurations. This structure can hold a maximum of 1 <code>S3DestinationConfiguration</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotDestinationConfiguration) -> dict:
    out: dict = {}
    if "s3_destinations" in value:
        import aws_sdk_quicksight.types.snapshot_s3_destination_configuration_list

        out["S3Destinations"] = (
            aws_sdk_quicksight.types.snapshot_s3_destination_configuration_list.serialize_json(
                value["s3_destinations"]
            )
        )
    return out


def deserialize_json(data: dict) -> SnapshotDestinationConfiguration:
    out: SnapshotDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if "S3Destinations" in data:
        import aws_sdk_quicksight.types.snapshot_s3_destination_configuration_list

        out["s3_destinations"] = (
            aws_sdk_quicksight.types.snapshot_s3_destination_configuration_list.deserialize_json(
                data["S3Destinations"]
            )
        )
    return out
