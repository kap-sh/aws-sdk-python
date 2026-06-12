"""Generated from Smithy shape ``com.amazonaws.datasync#DescribeLocationNfsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datasync.types.location_arn
    import aws_sdk_datasync.types.location_uri
    import aws_sdk_datasync.types.nfs_mount_options
    import aws_sdk_datasync.types.on_prem_config
    import aws_sdk_datasync.types.time


class DescribeLocationNfsResponse(TypedDict):
    location_arn: NotRequired["aws_sdk_datasync.types.location_arn.LocationArn"]
    """<p>The ARN of the NFS location.</p>"""
    location_uri: NotRequired["aws_sdk_datasync.types.location_uri.LocationUri"]
    """<p>The URI of the NFS location.</p>"""
    on_prem_config: NotRequired["aws_sdk_datasync.types.on_prem_config.OnPremConfig"]
    mount_options: NotRequired[
        "aws_sdk_datasync.types.nfs_mount_options.NfsMountOptions"
    ]
    """<p>The mount options that DataSync uses to mount your NFS file server.</p>"""
    creation_time: NotRequired["aws_sdk_datasync.types.time.Time"]
    """<p>The time when the NFS location was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLocationNfsResponse) -> dict:
    out: dict = {}
    if "location_arn" in value:
        out["LocationArn"] = value["location_arn"]
    if "location_uri" in value:
        out["LocationUri"] = value["location_uri"]
    if "on_prem_config" in value:
        import aws_sdk_datasync.types.on_prem_config

        out["OnPremConfig"] = (
            aws_sdk_datasync.types.on_prem_config.serialize_aws_json_1_1(
                value["on_prem_config"]
            )
        )
    if "mount_options" in value:
        import aws_sdk_datasync.types.nfs_mount_options

        out["MountOptions"] = (
            aws_sdk_datasync.types.nfs_mount_options.serialize_aws_json_1_1(
                value["mount_options"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_datasync.types.time

        out["CreationTime"] = aws_sdk_datasync.types.time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLocationNfsResponse:
    out: DescribeLocationNfsResponse = {}  # type: ignore[typeddict-item]
    if "LocationArn" in data:
        out["location_arn"] = data["LocationArn"]
    if "LocationUri" in data:
        out["location_uri"] = data["LocationUri"]
    if "OnPremConfig" in data:
        import aws_sdk_datasync.types.on_prem_config

        out["on_prem_config"] = (
            aws_sdk_datasync.types.on_prem_config.deserialize_aws_json_1_1(
                data["OnPremConfig"]
            )
        )
    if "MountOptions" in data:
        import aws_sdk_datasync.types.nfs_mount_options

        out["mount_options"] = (
            aws_sdk_datasync.types.nfs_mount_options.deserialize_aws_json_1_1(
                data["MountOptions"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_datasync.types.time

        out["creation_time"] = aws_sdk_datasync.types.time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    return out
