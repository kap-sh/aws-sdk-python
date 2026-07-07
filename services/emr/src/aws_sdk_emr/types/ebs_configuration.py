"""Generated from Smithy shape ``com.amazonaws.emr#EbsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.boolean_object
    import aws_sdk_emr.types.ebs_block_device_config_list


class EbsConfiguration(TypedDict, closed=True):
    ebs_block_device_configs: NotRequired[
        "aws_sdk_emr.types.ebs_block_device_config_list.EbsBlockDeviceConfigList"
    ]
    """<p>An array of Amazon EBS volume specifications attached to a cluster instance.</p>"""
    ebs_optimized: NotRequired["aws_sdk_emr.types.boolean_object.BooleanObject"]
    """<p>Indicates whether an Amazon EBS volume is EBS-optimized. The default is false. You should explicitly set this value to true to enable the Amazon EBS-optimized setting for an EC2 instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EbsConfiguration) -> dict:
    out: dict = {}
    if "ebs_block_device_configs" in value:
        import aws_sdk_emr.types.ebs_block_device_config_list

        out["EbsBlockDeviceConfigs"] = (
            aws_sdk_emr.types.ebs_block_device_config_list.serialize_aws_json_1_1(
                value["ebs_block_device_configs"]
            )
        )
    if "ebs_optimized" in value:
        out["EbsOptimized"] = value["ebs_optimized"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EbsConfiguration:
    out: EbsConfiguration = {}  # type: ignore[typeddict-item]
    if "EbsBlockDeviceConfigs" in data:
        import aws_sdk_emr.types.ebs_block_device_config_list

        out["ebs_block_device_configs"] = (
            aws_sdk_emr.types.ebs_block_device_config_list.deserialize_aws_json_1_1(
                data["EbsBlockDeviceConfigs"]
            )
        )
    if "EbsOptimized" in data:
        out["ebs_optimized"] = data["EbsOptimized"]
    return out
