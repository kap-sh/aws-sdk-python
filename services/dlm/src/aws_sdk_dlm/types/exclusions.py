"""Generated from Smithy shape ``com.amazonaws.dlm#Exclusions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dlm.types.exclude_boot_volumes
    import aws_sdk_dlm.types.exclude_tags_list
    import aws_sdk_dlm.types.exclude_volume_types_list


class Exclusions(TypedDict, closed=True):
    exclude_boot_volumes: NotRequired[
        "aws_sdk_dlm.types.exclude_boot_volumes.ExcludeBootVolumes"
    ]
    """<p> <b>[Default policies for EBS snapshots only]</b> Indicates whether to exclude volumes that are attached to instances as the boot volume. If you exclude boot volumes, only volumes attached as data (non-boot) volumes will be backed up by the policy. To exclude boot volumes, specify <code>true</code>.</p>"""
    exclude_volume_types: NotRequired[
        "aws_sdk_dlm.types.exclude_volume_types_list.ExcludeVolumeTypesList"
    ]
    """<p> <b>[Default policies for EBS snapshots only]</b> Specifies the volume types to exclude. Volumes of the specified types will not be targeted by the policy.</p>"""
    exclude_tags: NotRequired["aws_sdk_dlm.types.exclude_tags_list.ExcludeTagsList"]
    """<p> <b>[Default policies for EBS-backed AMIs only]</b> Specifies whether to exclude volumes that have specific tags. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Exclusions) -> dict:
    out: dict = {}
    if "exclude_boot_volumes" in value:
        out["ExcludeBootVolumes"] = value["exclude_boot_volumes"]
    if "exclude_volume_types" in value:
        import aws_sdk_dlm.types.exclude_volume_types_list

        out["ExcludeVolumeTypes"] = (
            aws_sdk_dlm.types.exclude_volume_types_list.serialize_json(
                value["exclude_volume_types"]
            )
        )
    if "exclude_tags" in value:
        import aws_sdk_dlm.types.exclude_tags_list

        out["ExcludeTags"] = aws_sdk_dlm.types.exclude_tags_list.serialize_json(
            value["exclude_tags"]
        )
    return out


def deserialize_json(data: dict) -> Exclusions:
    out: Exclusions = {}  # type: ignore[typeddict-item]
    if "ExcludeBootVolumes" in data:
        out["exclude_boot_volumes"] = data["ExcludeBootVolumes"]
    if "ExcludeVolumeTypes" in data:
        import aws_sdk_dlm.types.exclude_volume_types_list

        out["exclude_volume_types"] = (
            aws_sdk_dlm.types.exclude_volume_types_list.deserialize_json(
                data["ExcludeVolumeTypes"]
            )
        )
    if "ExcludeTags" in data:
        import aws_sdk_dlm.types.exclude_tags_list

        out["exclude_tags"] = aws_sdk_dlm.types.exclude_tags_list.deserialize_json(
            data["ExcludeTags"]
        )
    return out
