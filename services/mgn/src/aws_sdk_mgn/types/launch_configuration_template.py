"""Generated from Smithy shape ``com.amazonaws.mgn#LaunchConfigurationTemplate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.arn
    import aws_sdk_mgn.types.boot_mode
    import aws_sdk_mgn.types.ec2_launch_configuration_template_id
    import aws_sdk_mgn.types.launch_configuration_template_id
    import aws_sdk_mgn.types.launch_disposition
    import aws_sdk_mgn.types.launch_template_disk_conf
    import aws_sdk_mgn.types.licensing
    import aws_sdk_mgn.types.positive_integer
    import aws_sdk_mgn.types.post_launch_actions
    import aws_sdk_mgn.types.tag_value
    import aws_sdk_mgn.types.tags_map
    import aws_sdk_mgn.types.target_instance_type_right_sizing_method


class LaunchConfigurationTemplate(TypedDict):
    launch_configuration_template_id: "aws_sdk_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID"
    """<p>ID of the Launch Configuration Template.</p>"""
    arn: NotRequired["aws_sdk_mgn.types.arn.ARN"]
    """<p>ARN of the Launch Configuration Template.</p>"""
    post_launch_actions: NotRequired[
        "aws_sdk_mgn.types.post_launch_actions.PostLaunchActions"
    ]
    """<p>Post Launch Actions of the Launch Configuration Template.</p>"""
    enable_map_auto_tagging: NotRequired["bool"]
    """<p>Enable map auto tagging.</p>"""
    map_auto_tagging_mpe_id: NotRequired["aws_sdk_mgn.types.tag_value.TagValue"]
    """<p>Launch configuration template map auto tagging MPE ID.</p>"""
    tags: NotRequired["aws_sdk_mgn.types.tags_map.TagsMap"]
    """<p>Tags of the Launch Configuration Template.</p>"""
    ec2_launch_template_id: NotRequired[
        "aws_sdk_mgn.types.ec2_launch_configuration_template_id.EC2LaunchConfigurationTemplateID"
    ]
    """<p>EC2 launch template ID.</p>"""
    launch_disposition: NotRequired[
        "aws_sdk_mgn.types.launch_disposition.LaunchDisposition"
    ]
    """<p>Launch disposition.</p>"""
    target_instance_type_right_sizing_method: NotRequired[
        "aws_sdk_mgn.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
    ]
    """<p>Target instance type right-sizing method.</p>"""
    copy_private_ip: NotRequired["bool"]
    """<p>Copy private Ip.</p>"""
    associate_public_ip_address: NotRequired["bool"]
    """<p>Associate public Ip address.</p>"""
    copy_tags: NotRequired["bool"]
    """<p>Copy tags.</p>"""
    licensing: NotRequired["aws_sdk_mgn.types.licensing.Licensing"]
    boot_mode: NotRequired["aws_sdk_mgn.types.boot_mode.BootMode"]
    """<p>Launch configuration template boot mode.</p>"""
    small_volume_max_size: "aws_sdk_mgn.types.positive_integer.PositiveInteger"
    """<p>Small volume maximum size.</p>"""
    small_volume_conf: NotRequired[
        "aws_sdk_mgn.types.launch_template_disk_conf.LaunchTemplateDiskConf"
    ]
    """<p>Small volume config.</p>"""
    large_volume_conf: NotRequired[
        "aws_sdk_mgn.types.launch_template_disk_conf.LaunchTemplateDiskConf"
    ]
    """<p>Large volume config.</p>"""
    enable_parameters_encryption: NotRequired["bool"]
    """<p>Enable parameters encryption.</p>"""
    parameters_encryption_key: NotRequired["aws_sdk_mgn.types.arn.ARN"]
    """<p>Parameters encryption key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LaunchConfigurationTemplate) -> dict:
    out: dict = {}
    out["launchConfigurationTemplateID"] = value["launch_configuration_template_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "post_launch_actions" in value:
        import aws_sdk_mgn.types.post_launch_actions

        out["postLaunchActions"] = aws_sdk_mgn.types.post_launch_actions.serialize_json(
            value["post_launch_actions"]
        )
    if "enable_map_auto_tagging" in value:
        out["enableMapAutoTagging"] = value["enable_map_auto_tagging"]
    if "map_auto_tagging_mpe_id" in value:
        out["mapAutoTaggingMpeID"] = value["map_auto_tagging_mpe_id"]
    if "tags" in value:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.serialize_json(value["tags"])
    if "ec2_launch_template_id" in value:
        out["ec2LaunchTemplateID"] = value["ec2_launch_template_id"]
    if "launch_disposition" in value:
        out["launchDisposition"] = value["launch_disposition"]
    if "target_instance_type_right_sizing_method" in value:
        out["targetInstanceTypeRightSizingMethod"] = value[
            "target_instance_type_right_sizing_method"
        ]
    if "copy_private_ip" in value:
        out["copyPrivateIp"] = value["copy_private_ip"]
    if "associate_public_ip_address" in value:
        out["associatePublicIpAddress"] = value["associate_public_ip_address"]
    if "copy_tags" in value:
        out["copyTags"] = value["copy_tags"]
    if "licensing" in value:
        import aws_sdk_mgn.types.licensing

        out["licensing"] = aws_sdk_mgn.types.licensing.serialize_json(
            value["licensing"]
        )
    if "boot_mode" in value:
        out["bootMode"] = value["boot_mode"]
    out["smallVolumeMaxSize"] = value.get("small_volume_max_size", 0)
    if "small_volume_conf" in value:
        import aws_sdk_mgn.types.launch_template_disk_conf

        out["smallVolumeConf"] = (
            aws_sdk_mgn.types.launch_template_disk_conf.serialize_json(
                value["small_volume_conf"]
            )
        )
    if "large_volume_conf" in value:
        import aws_sdk_mgn.types.launch_template_disk_conf

        out["largeVolumeConf"] = (
            aws_sdk_mgn.types.launch_template_disk_conf.serialize_json(
                value["large_volume_conf"]
            )
        )
    if "enable_parameters_encryption" in value:
        out["enableParametersEncryption"] = value["enable_parameters_encryption"]
    if "parameters_encryption_key" in value:
        out["parametersEncryptionKey"] = value["parameters_encryption_key"]
    return out


def deserialize_json(data: dict) -> LaunchConfigurationTemplate:
    out: LaunchConfigurationTemplate = {}  # type: ignore[typeddict-item]
    if "launchConfigurationTemplateID" in data:
        out["launch_configuration_template_id"] = data["launchConfigurationTemplateID"]
    else:
        raise DeserializationError(
            "LaunchConfigurationTemplate.launch_configuration_template_id required"
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    if "postLaunchActions" in data:
        import aws_sdk_mgn.types.post_launch_actions

        out["post_launch_actions"] = (
            aws_sdk_mgn.types.post_launch_actions.deserialize_json(
                data["postLaunchActions"]
            )
        )
    if "enableMapAutoTagging" in data:
        out["enable_map_auto_tagging"] = data["enableMapAutoTagging"]
    if "mapAutoTaggingMpeID" in data:
        out["map_auto_tagging_mpe_id"] = data["mapAutoTaggingMpeID"]
    if "tags" in data:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.deserialize_json(data["tags"])
    if "ec2LaunchTemplateID" in data:
        out["ec2_launch_template_id"] = data["ec2LaunchTemplateID"]
    if "launchDisposition" in data:
        out["launch_disposition"] = data["launchDisposition"]
    if "targetInstanceTypeRightSizingMethod" in data:
        out["target_instance_type_right_sizing_method"] = data[
            "targetInstanceTypeRightSizingMethod"
        ]
    if "copyPrivateIp" in data:
        out["copy_private_ip"] = data["copyPrivateIp"]
    if "associatePublicIpAddress" in data:
        out["associate_public_ip_address"] = data["associatePublicIpAddress"]
    if "copyTags" in data:
        out["copy_tags"] = data["copyTags"]
    if "licensing" in data:
        import aws_sdk_mgn.types.licensing

        out["licensing"] = aws_sdk_mgn.types.licensing.deserialize_json(
            data["licensing"]
        )
    if "bootMode" in data:
        out["boot_mode"] = data["bootMode"]
    if "smallVolumeMaxSize" in data:
        out["small_volume_max_size"] = data["smallVolumeMaxSize"]
    else:
        out["small_volume_max_size"] = 0
    if "smallVolumeConf" in data:
        import aws_sdk_mgn.types.launch_template_disk_conf

        out["small_volume_conf"] = (
            aws_sdk_mgn.types.launch_template_disk_conf.deserialize_json(
                data["smallVolumeConf"]
            )
        )
    if "largeVolumeConf" in data:
        import aws_sdk_mgn.types.launch_template_disk_conf

        out["large_volume_conf"] = (
            aws_sdk_mgn.types.launch_template_disk_conf.deserialize_json(
                data["largeVolumeConf"]
            )
        )
    if "enableParametersEncryption" in data:
        out["enable_parameters_encryption"] = data["enableParametersEncryption"]
    if "parametersEncryptionKey" in data:
        out["parameters_encryption_key"] = data["parametersEncryptionKey"]
    return out
