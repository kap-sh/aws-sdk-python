"""Generated from Smithy shape ``com.amazonaws.fsx#DeleteVolumeOpenZFSConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.delete_open_zfs_volume_options


class DeleteVolumeOpenZFSConfiguration(TypedDict, closed=True):
    options: NotRequired[
        "capo_fsx.types.delete_open_zfs_volume_options.DeleteOpenZFSVolumeOptions"
    ]
    """<p>To delete the volume's child volumes, snapshots, and clones, use the string <code>DELETE_CHILD_VOLUMES_AND_SNAPSHOTS</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteVolumeOpenZFSConfiguration) -> dict:
    out: dict = {}
    if "options" in value:
        import capo_fsx.types.delete_open_zfs_volume_options

        out["Options"] = (
            capo_fsx.types.delete_open_zfs_volume_options.serialize_aws_json_1_1(
                value["options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteVolumeOpenZFSConfiguration:
    out: DeleteVolumeOpenZFSConfiguration = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import capo_fsx.types.delete_open_zfs_volume_options

        out["options"] = (
            capo_fsx.types.delete_open_zfs_volume_options.deserialize_aws_json_1_1(
                data["Options"]
            )
        )
    return out
