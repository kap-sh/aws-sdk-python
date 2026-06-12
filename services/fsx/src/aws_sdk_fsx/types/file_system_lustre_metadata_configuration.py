"""Generated from Smithy shape ``com.amazonaws.fsx#FileSystemLustreMetadataConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.metadata_configuration_mode
    import aws_sdk_fsx.types.metadata_iops


class FileSystemLustreMetadataConfiguration(TypedDict):
    iops: NotRequired["aws_sdk_fsx.types.metadata_iops.MetadataIops"]
    """<p>The number of Metadata IOPS provisioned for the file system.</p> <ul> <li> <p>For SSD file systems, valid values are <code>1500</code>, <code>3000</code>, <code>6000</code>, <code>12000</code>, and multiples of <code>12000</code> up to a maximum of <code>192000</code>.</p> </li> <li> <p>For Intelligent-Tiering file systems, valid values are <code>6000</code> and <code>12000</code>.</p> </li> </ul>"""
    mode: NotRequired[
        "aws_sdk_fsx.types.metadata_configuration_mode.MetadataConfigurationMode"
    ]
    """<p>The metadata configuration mode for provisioning Metadata IOPS for the file system.</p> <ul> <li> <p>In AUTOMATIC mode (supported only on SSD file systems), FSx for Lustre automatically provisions and scales the number of Metadata IOPS on your file system based on your file system storage capacity.</p> </li> <li> <p>In USER_PROVISIONED mode, you can choose to specify the number of Metadata IOPS to provision for your file system.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSystemLustreMetadataConfiguration) -> dict:
    out: dict = {}
    if "iops" in value:
        out["Iops"] = value["iops"]
    if "mode" in value:
        import aws_sdk_fsx.types.metadata_configuration_mode

        out["Mode"] = (
            aws_sdk_fsx.types.metadata_configuration_mode.serialize_aws_json_1_1(
                value["mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FileSystemLustreMetadataConfiguration:
    out: FileSystemLustreMetadataConfiguration = {}  # type: ignore[typeddict-item]
    if "Iops" in data:
        out["iops"] = data["Iops"]
    if "Mode" in data:
        import aws_sdk_fsx.types.metadata_configuration_mode

        out["mode"] = (
            aws_sdk_fsx.types.metadata_configuration_mode.deserialize_aws_json_1_1(
                data["Mode"]
            )
        )
    return out
