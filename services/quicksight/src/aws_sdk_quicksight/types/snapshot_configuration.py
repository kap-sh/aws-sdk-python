"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.parameters
    import aws_sdk_quicksight.types.snapshot_destination_configuration
    import aws_sdk_quicksight.types.snapshot_file_group_list


class SnapshotConfiguration(TypedDict):
    file_groups: (
        "aws_sdk_quicksight.types.snapshot_file_group_list.SnapshotFileGroupList"
    )
    """<p>A list of <code>SnapshotJobResultFileGroup</code> objects that contain information about the snapshot that is generated. This list can hold a maximum of 6 <code>FileGroup</code> configurations.</p>"""
    destination_configuration: NotRequired[
        "aws_sdk_quicksight.types.snapshot_destination_configuration.SnapshotDestinationConfiguration"
    ]
    """<p>A structure that contains information on the Amazon S3 bucket that the generated snapshot is stored in.</p>"""
    parameters: NotRequired["aws_sdk_quicksight.types.parameters.Parameters"]


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.snapshot_file_group_list

    out["FileGroups"] = (
        aws_sdk_quicksight.types.snapshot_file_group_list.serialize_json(
            value["file_groups"]
        )
    )
    if "destination_configuration" in value:
        import aws_sdk_quicksight.types.snapshot_destination_configuration

        out["DestinationConfiguration"] = (
            aws_sdk_quicksight.types.snapshot_destination_configuration.serialize_json(
                value["destination_configuration"]
            )
        )
    if "parameters" in value:
        import aws_sdk_quicksight.types.parameters

        out["Parameters"] = aws_sdk_quicksight.types.parameters.serialize_json(
            value["parameters"]
        )
    return out


def deserialize_json(data: dict) -> SnapshotConfiguration:
    out: SnapshotConfiguration = {}  # type: ignore[typeddict-item]
    if "FileGroups" in data:
        import aws_sdk_quicksight.types.snapshot_file_group_list

        out["file_groups"] = (
            aws_sdk_quicksight.types.snapshot_file_group_list.deserialize_json(
                data["FileGroups"]
            )
        )
    else:
        raise DeserializationError("SnapshotConfiguration.file_groups required")
    if "DestinationConfiguration" in data:
        import aws_sdk_quicksight.types.snapshot_destination_configuration

        out["destination_configuration"] = (
            aws_sdk_quicksight.types.snapshot_destination_configuration.deserialize_json(
                data["DestinationConfiguration"]
            )
        )
    if "Parameters" in data:
        import aws_sdk_quicksight.types.parameters

        out["parameters"] = aws_sdk_quicksight.types.parameters.deserialize_json(
            data["Parameters"]
        )
    return out
