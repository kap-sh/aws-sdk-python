"""Generated from Smithy shape ``com.amazonaws.dlm#Parameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dlm.types.exclude_boot_volume
    import aws_sdk_dlm.types.exclude_data_volume_tag_list
    import aws_sdk_dlm.types.no_reboot


class Parameters(TypedDict):
    exclude_boot_volume: NotRequired[
        "aws_sdk_dlm.types.exclude_boot_volume.ExcludeBootVolume"
    ]
    """<p> <b>[Custom snapshot policies that target instances only]</b> Indicates whether to exclude the root volume from multi-volume snapshot sets. The default is <code>false</code>. If you specify <code>true</code>, then the root volumes attached to targeted instances will be excluded from the multi-volume snapshot sets created by the policy.</p>"""
    no_reboot: NotRequired["aws_sdk_dlm.types.no_reboot.NoReboot"]
    """<p> <b>[Custom AMI policies only]</b> Indicates whether targeted instances are rebooted when the lifecycle policy runs. <code>true</code> indicates that targeted instances are not rebooted when the policy runs. <code>false</code> indicates that target instances are rebooted when the policy runs. The default is <code>true</code> (instances are not rebooted).</p>"""
    exclude_data_volume_tags: NotRequired[
        "aws_sdk_dlm.types.exclude_data_volume_tag_list.ExcludeDataVolumeTagList"
    ]
    """<p> <b>[Custom snapshot policies that target instances only]</b> The tags used to identify data (non-root) volumes to exclude from multi-volume snapshot sets.</p> <p>If you create a snapshot lifecycle policy that targets instances and you specify tags for this parameter, then data volumes with the specified tags that are attached to targeted instances will be excluded from the multi-volume snapshot sets created by the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Parameters) -> dict:
    out: dict = {}
    if "exclude_boot_volume" in value:
        out["ExcludeBootVolume"] = value["exclude_boot_volume"]
    if "no_reboot" in value:
        out["NoReboot"] = value["no_reboot"]
    if "exclude_data_volume_tags" in value:
        import aws_sdk_dlm.types.exclude_data_volume_tag_list

        out["ExcludeDataVolumeTags"] = (
            aws_sdk_dlm.types.exclude_data_volume_tag_list.serialize_json(
                value["exclude_data_volume_tags"]
            )
        )
    return out


def deserialize_json(data: dict) -> Parameters:
    out: Parameters = {}  # type: ignore[typeddict-item]
    if "ExcludeBootVolume" in data:
        out["exclude_boot_volume"] = data["ExcludeBootVolume"]
    if "NoReboot" in data:
        out["no_reboot"] = data["NoReboot"]
    if "ExcludeDataVolumeTags" in data:
        import aws_sdk_dlm.types.exclude_data_volume_tag_list

        out["exclude_data_volume_tags"] = (
            aws_sdk_dlm.types.exclude_data_volume_tag_list.deserialize_json(
                data["ExcludeDataVolumeTags"]
            )
        )
    return out
