"""Generated from Smithy shape ``com.amazonaws.batch#Volume``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.efs_volume_configuration
    import aws_sdk_batch.types.host
    import aws_sdk_batch.types.s3_files_volume_configuration
    import aws_sdk_batch.types.string


class Volume(TypedDict):
    host: NotRequired["aws_sdk_batch.types.host.Host"]
    """<p>The contents of the <code>host</code> parameter determine whether your data volume persists on the host container instance and where it's stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data isn't guaranteed to persist after the containers that are associated with it stop running.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.</p> </note>"""
    name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the volume. It can be up to 255 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_). This name is referenced in the <code>sourceVolume</code> parameter of container definition <code>mountPoints</code>.</p>"""
    efs_volume_configuration: NotRequired[
        "aws_sdk_batch.types.efs_volume_configuration.EFSVolumeConfiguration"
    ]
    """<p>This parameter is specified when you're using an Amazon Elastic File System file system for job storage. Jobs that are running on Fargate resources must specify a <code>platformVersion</code> of at least <code>1.4.0</code>.</p>"""
    s3files_volume_configuration: NotRequired[
        "aws_sdk_batch.types.s3_files_volume_configuration.S3FilesVolumeConfiguration"
    ]
    """<p>This parameter is specified when you're using an S3Files file system for job storage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Volume) -> dict:
    out: dict = {}
    if "host" in value:
        import aws_sdk_batch.types.host

        out["host"] = aws_sdk_batch.types.host.serialize_json(value["host"])
    if "name" in value:
        out["name"] = value["name"]
    if "efs_volume_configuration" in value:
        import aws_sdk_batch.types.efs_volume_configuration

        out["efsVolumeConfiguration"] = (
            aws_sdk_batch.types.efs_volume_configuration.serialize_json(
                value["efs_volume_configuration"]
            )
        )
    if "s3files_volume_configuration" in value:
        import aws_sdk_batch.types.s3_files_volume_configuration

        out["s3filesVolumeConfiguration"] = (
            aws_sdk_batch.types.s3_files_volume_configuration.serialize_json(
                value["s3files_volume_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> Volume:
    out: Volume = {}  # type: ignore[typeddict-item]
    if "host" in data:
        import aws_sdk_batch.types.host

        out["host"] = aws_sdk_batch.types.host.deserialize_json(data["host"])
    if "name" in data:
        out["name"] = data["name"]
    if "efsVolumeConfiguration" in data:
        import aws_sdk_batch.types.efs_volume_configuration

        out["efs_volume_configuration"] = (
            aws_sdk_batch.types.efs_volume_configuration.deserialize_json(
                data["efsVolumeConfiguration"]
            )
        )
    if "s3filesVolumeConfiguration" in data:
        import aws_sdk_batch.types.s3_files_volume_configuration

        out["s3files_volume_configuration"] = (
            aws_sdk_batch.types.s3_files_volume_configuration.deserialize_json(
                data["s3filesVolumeConfiguration"]
            )
        )
    return out
