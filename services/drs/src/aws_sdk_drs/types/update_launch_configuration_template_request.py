"""Generated from Smithy shape ``com.amazonaws.drs#UpdateLaunchConfigurationTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_drs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_drs.types.arn
    import aws_sdk_drs.types.launch_configuration_template_id
    import aws_sdk_drs.types.launch_disposition
    import aws_sdk_drs.types.licensing
    import aws_sdk_drs.types.target_instance_type_right_sizing_method


class UpdateLaunchConfigurationTemplateRequest(TypedDict, closed=True):
    launch_configuration_template_id: "aws_sdk_drs.types.launch_configuration_template_id.LaunchConfigurationTemplateID"
    """<p>Launch Configuration Template ID.</p>"""
    launch_disposition: NotRequired[
        "aws_sdk_drs.types.launch_disposition.LaunchDisposition"
    ]
    """<p>Launch disposition.</p>"""
    target_instance_type_right_sizing_method: NotRequired[
        "aws_sdk_drs.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
    ]
    """<p>Target instance type right-sizing method.</p>"""
    copy_private_ip: NotRequired["bool"]
    """<p>Copy private IP.</p>"""
    copy_tags: NotRequired["bool"]
    """<p>Copy tags.</p>"""
    licensing: NotRequired["aws_sdk_drs.types.licensing.Licensing"]
    """<p>Licensing.</p>"""
    export_bucket_arn: NotRequired["aws_sdk_drs.types.arn.ARN"]
    """<p>S3 bucket ARN to export Source Network templates.</p>"""
    post_launch_enabled: NotRequired["bool"]
    """<p>Whether we want to activate post-launch actions.</p>"""
    launch_into_source_instance: NotRequired["bool"]
    """<p>DRS will set the 'launch into instance ID' of any source server when performing a drill, recovery or failback to the previous region or availability zone, using the instance ID of the source instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLaunchConfigurationTemplateRequest) -> dict:
    out: dict = {}
    out["launchConfigurationTemplateID"] = value["launch_configuration_template_id"]
    if "launch_disposition" in value:
        out["launchDisposition"] = value["launch_disposition"]
    if "target_instance_type_right_sizing_method" in value:
        out["targetInstanceTypeRightSizingMethod"] = value[
            "target_instance_type_right_sizing_method"
        ]
    if "copy_private_ip" in value:
        out["copyPrivateIp"] = value["copy_private_ip"]
    if "copy_tags" in value:
        out["copyTags"] = value["copy_tags"]
    if "licensing" in value:
        import aws_sdk_drs.types.licensing

        out["licensing"] = aws_sdk_drs.types.licensing.serialize_json(
            value["licensing"]
        )
    if "export_bucket_arn" in value:
        out["exportBucketArn"] = value["export_bucket_arn"]
    if "post_launch_enabled" in value:
        out["postLaunchEnabled"] = value["post_launch_enabled"]
    if "launch_into_source_instance" in value:
        out["launchIntoSourceInstance"] = value["launch_into_source_instance"]
    return out


def deserialize_json(data: dict) -> UpdateLaunchConfigurationTemplateRequest:
    out: UpdateLaunchConfigurationTemplateRequest = {}  # type: ignore[typeddict-item]
    if "launchConfigurationTemplateID" in data:
        out["launch_configuration_template_id"] = data["launchConfigurationTemplateID"]
    else:
        raise DeserializationError(
            "UpdateLaunchConfigurationTemplateRequest.launch_configuration_template_id required"
        )
    if "launchDisposition" in data:
        out["launch_disposition"] = data["launchDisposition"]
    if "targetInstanceTypeRightSizingMethod" in data:
        out["target_instance_type_right_sizing_method"] = data[
            "targetInstanceTypeRightSizingMethod"
        ]
    if "copyPrivateIp" in data:
        out["copy_private_ip"] = data["copyPrivateIp"]
    if "copyTags" in data:
        out["copy_tags"] = data["copyTags"]
    if "licensing" in data:
        import aws_sdk_drs.types.licensing

        out["licensing"] = aws_sdk_drs.types.licensing.deserialize_json(
            data["licensing"]
        )
    if "exportBucketArn" in data:
        out["export_bucket_arn"] = data["exportBucketArn"]
    if "postLaunchEnabled" in data:
        out["post_launch_enabled"] = data["postLaunchEnabled"]
    if "launchIntoSourceInstance" in data:
        out["launch_into_source_instance"] = data["launchIntoSourceInstance"]
    return out
