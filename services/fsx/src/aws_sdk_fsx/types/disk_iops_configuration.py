"""Generated from Smithy shape ``com.amazonaws.fsx#DiskIopsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.disk_iops_configuration_mode
    import aws_sdk_fsx.types.iops


class DiskIopsConfiguration(TypedDict, closed=True):
    mode: NotRequired[
        "aws_sdk_fsx.types.disk_iops_configuration_mode.DiskIopsConfigurationMode"
    ]
    """<p>Specifies whether the file system is using the <code>AUTOMATIC</code> setting of SSD IOPS of 3 IOPS per GB of storage capacity, or if it using a <code>USER_PROVISIONED</code> value.</p>"""
    iops: NotRequired["aws_sdk_fsx.types.iops.Iops"]
    """<p>The total number of SSD IOPS provisioned for the file system.</p> <p>The minimum and maximum values for this property depend on the value of <code>HAPairs</code> and <code>StorageCapacity</code>. The minimum value is calculated as <code>StorageCapacity</code> * 3 * <code>HAPairs</code> (3 IOPS per GB of <code>StorageCapacity</code>). The maximum value is calculated as 200,000 * <code>HAPairs</code>.</p> <p>Amazon FSx responds with an HTTP status code 400 (Bad Request) if the value of <code>Iops</code> is outside of the minimum or maximum values.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiskIopsConfiguration) -> dict:
    out: dict = {}
    if "mode" in value:
        import aws_sdk_fsx.types.disk_iops_configuration_mode

        out["Mode"] = (
            aws_sdk_fsx.types.disk_iops_configuration_mode.serialize_aws_json_1_1(
                value["mode"]
            )
        )
    if "iops" in value:
        out["Iops"] = value["iops"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DiskIopsConfiguration:
    out: DiskIopsConfiguration = {}  # type: ignore[typeddict-item]
    if "Mode" in data:
        import aws_sdk_fsx.types.disk_iops_configuration_mode

        out["mode"] = (
            aws_sdk_fsx.types.disk_iops_configuration_mode.deserialize_aws_json_1_1(
                data["Mode"]
            )
        )
    if "Iops" in data:
        out["iops"] = data["Iops"]
    return out
