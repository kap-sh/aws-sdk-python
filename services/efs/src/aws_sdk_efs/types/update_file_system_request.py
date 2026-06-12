"""Generated from Smithy shape ``com.amazonaws.efs#UpdateFileSystemRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_efs.types.file_system_id
    import aws_sdk_efs.types.provisioned_throughput_in_mibps
    import aws_sdk_efs.types.throughput_mode


class UpdateFileSystemRequest(TypedDict):
    file_system_id: "aws_sdk_efs.types.file_system_id.FileSystemId"
    """<p>The ID of the file system that you want to update.</p>"""
    throughput_mode: NotRequired["aws_sdk_efs.types.throughput_mode.ThroughputMode"]
    """<p>(Optional) Updates the file system's throughput mode. If you're not updating your throughput mode, you don't need to provide this value in your request. If you are changing the <code>ThroughputMode</code> to <code>provisioned</code>, you must also set a value for <code>ProvisionedThroughputInMibps</code>.</p>"""
    provisioned_throughput_in_mibps: NotRequired[
        "aws_sdk_efs.types.provisioned_throughput_in_mibps.ProvisionedThroughputInMibps"
    ]
    """<p>(Optional) The throughput, measured in mebibytes per second (MiBps), that you want to provision for a file system that you're creating. Required if <code>ThroughputMode</code> is set to <code>provisioned</code>. Valid values are 1-3414 MiBps, with the upper limit depending on Region. To increase this limit, contact Amazon Web Services Support. For more information, see <a href=\"https://docs.aws.amazon.com/efs/latest/ug/limits.html#soft-limits\">Amazon EFS quotas that you can increase</a> in the <i>Amazon EFS User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFileSystemRequest) -> dict:
    out: dict = {}
    if "throughput_mode" in value:
        import aws_sdk_efs.types.throughput_mode

        out["ThroughputMode"] = aws_sdk_efs.types.throughput_mode.serialize_json(
            value["throughput_mode"]
        )
    if "provisioned_throughput_in_mibps" in value:
        out["ProvisionedThroughputInMibps"] = value["provisioned_throughput_in_mibps"]
    return out


def deserialize_json(data: dict) -> UpdateFileSystemRequest:
    out: UpdateFileSystemRequest = {}  # type: ignore[typeddict-item]
    if "ThroughputMode" in data:
        import aws_sdk_efs.types.throughput_mode

        out["throughput_mode"] = aws_sdk_efs.types.throughput_mode.deserialize_json(
            data["ThroughputMode"]
        )
    if "ProvisionedThroughputInMibps" in data:
        out["provisioned_throughput_in_mibps"] = data["ProvisionedThroughputInMibps"]
    return out
