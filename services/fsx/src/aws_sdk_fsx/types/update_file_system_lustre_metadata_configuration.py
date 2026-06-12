"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateFileSystemLustreMetadataConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.metadata_configuration_mode
    import aws_sdk_fsx.types.metadata_iops


class UpdateFileSystemLustreMetadataConfiguration(TypedDict):
    iops: NotRequired["aws_sdk_fsx.types.metadata_iops.MetadataIops"]
    """<p>(USER_PROVISIONED mode only) Specifies the number of Metadata IOPS to provision for your file system.</p> <ul> <li> <p>For SSD file systems, valid values are <code>1500</code>, <code>3000</code>, <code>6000</code>, <code>12000</code>, and multiples of <code>12000</code> up to a maximum of <code>192000</code>.</p> </li> <li> <p>For Intelligent-Tiering file systems, valid values are <code>6000</code> and <code>12000</code>.</p> </li> </ul> <p>The value you provide must be greater than or equal to the current number of Metadata IOPS provisioned for the file system.</p>"""
    mode: NotRequired[
        "aws_sdk_fsx.types.metadata_configuration_mode.MetadataConfigurationMode"
    ]
    """<p>The metadata configuration mode for provisioning Metadata IOPS for an FSx for Lustre file system using a <code>PERSISTENT_2</code> deployment type.</p> <ul> <li> <p>To increase the Metadata IOPS or to switch an SSD file system from AUTOMATIC, specify <code>USER_PROVISIONED</code> as the value for this parameter. Then use the Iops parameter to provide a Metadata IOPS value that is greater than or equal to the current number of Metadata IOPS provisioned for the file system.</p> </li> <li> <p>To switch from USER_PROVISIONED mode on an SSD file system, specify <code>AUTOMATIC</code> as the value for this parameter, but do not input a value for Iops.</p> <note> <ul> <li> <p>If you request to switch from USER_PROVISIONED to AUTOMATIC mode and the current Metadata IOPS value is greater than the automated default, FSx for Lustre rejects the request because downscaling Metadata IOPS is not supported.</p> </li> <li> <p>AUTOMATIC mode is not supported on Intelligent-Tiering file systems. For Intelligent-Tiering file systems, use USER_PROVISIONED mode.</p> </li> </ul> </note> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFileSystemLustreMetadataConfiguration) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> UpdateFileSystemLustreMetadataConfiguration:
    out: UpdateFileSystemLustreMetadataConfiguration = {}  # type: ignore[typeddict-item]
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
