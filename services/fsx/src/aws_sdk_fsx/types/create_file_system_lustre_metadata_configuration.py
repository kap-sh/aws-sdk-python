"""Generated from Smithy shape ``com.amazonaws.fsx#CreateFileSystemLustreMetadataConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.metadata_configuration_mode
    import aws_sdk_fsx.types.metadata_iops


class CreateFileSystemLustreMetadataConfiguration(TypedDict):
    iops: NotRequired["aws_sdk_fsx.types.metadata_iops.MetadataIops"]
    """<p>(USER_PROVISIONED mode only) Specifies the number of Metadata IOPS to provision for the file system. This parameter sets the maximum rate of metadata disk IOPS supported by the file system.</p> <ul> <li> <p>For SSD file systems, valid values are <code>1500</code>, <code>3000</code>, <code>6000</code>, <code>12000</code>, and multiples of <code>12000</code> up to a maximum of <code>192000</code>.</p> </li> <li> <p>For Intelligent-Tiering file systems, valid values are <code>6000</code> and <code>12000</code>.</p> </li> </ul> <note> <p> <code>Iops</code> doesn’t have a default value. If you're using USER_PROVISIONED mode, you can choose to specify a valid value. If you're using AUTOMATIC mode, you cannot specify a value because FSx for Lustre automatically sets the value based on your file system storage capacity. </p> </note>"""
    mode: NotRequired[
        "aws_sdk_fsx.types.metadata_configuration_mode.MetadataConfigurationMode"
    ]
    """<p>The metadata configuration mode for provisioning Metadata IOPS for an FSx for Lustre file system using a <code>PERSISTENT_2</code> deployment type.</p> <ul> <li> <p>In AUTOMATIC mode (supported only on SSD file systems), FSx for Lustre automatically provisions and scales the number of Metadata IOPS for your file system based on your file system storage capacity.</p> </li> <li> <p>In USER_PROVISIONED mode, you specify the number of Metadata IOPS to provision for your file system.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFileSystemLustreMetadataConfiguration) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> CreateFileSystemLustreMetadataConfiguration:
    out: CreateFileSystemLustreMetadataConfiguration = {}  # type: ignore[typeddict-item]
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
