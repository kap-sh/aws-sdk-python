"""Generated from Smithy shape ``com.amazonaws.drs#UpdateLaunchConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_drs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_drs.types.launch_disposition
    import aws_sdk_drs.types.launch_into_instance_properties
    import aws_sdk_drs.types.licensing
    import aws_sdk_drs.types.small_bounded_string
    import aws_sdk_drs.types.source_server_id
    import aws_sdk_drs.types.target_instance_type_right_sizing_method


class UpdateLaunchConfigurationRequest(TypedDict):
    source_server_id: "aws_sdk_drs.types.source_server_id.SourceServerID"
    """<p>The ID of the Source Server that we want to retrieve a Launch Configuration for.</p>"""
    name: NotRequired["aws_sdk_drs.types.small_bounded_string.SmallBoundedString"]
    """<p>The name of the launch configuration.</p>"""
    launch_disposition: NotRequired[
        "aws_sdk_drs.types.launch_disposition.LaunchDisposition"
    ]
    """<p>The state of the Recovery Instance in EC2 after the recovery operation.</p>"""
    target_instance_type_right_sizing_method: NotRequired[
        "aws_sdk_drs.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
    ]
    """<p>Whether Elastic Disaster Recovery should try to automatically choose the instance type that best matches the OS, CPU, and RAM of your Source Server.</p>"""
    copy_private_ip: NotRequired["bool"]
    """<p>Whether we should copy the Private IP of the Source Server to the Recovery Instance.</p>"""
    copy_tags: NotRequired["bool"]
    """<p>Whether we want to copy the tags of the Source Server to the EC2 machine of the Recovery Instance.</p>"""
    licensing: NotRequired["aws_sdk_drs.types.licensing.Licensing"]
    """<p>The licensing configuration to be used for this launch configuration.</p>"""
    post_launch_enabled: NotRequired["bool"]
    """<p>Whether we want to enable post-launch actions for the Source Server.</p>"""
    launch_into_instance_properties: NotRequired[
        "aws_sdk_drs.types.launch_into_instance_properties.LaunchIntoInstanceProperties"
    ]
    """<p>Launch into existing instance properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLaunchConfigurationRequest) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    if "name" in value:
        out["name"] = value["name"]
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
    if "post_launch_enabled" in value:
        out["postLaunchEnabled"] = value["post_launch_enabled"]
    if "launch_into_instance_properties" in value:
        import aws_sdk_drs.types.launch_into_instance_properties

        out["launchIntoInstanceProperties"] = (
            aws_sdk_drs.types.launch_into_instance_properties.serialize_json(
                value["launch_into_instance_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateLaunchConfigurationRequest:
    out: UpdateLaunchConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "sourceServerID" in data:
        out["source_server_id"] = data["sourceServerID"]
    else:
        raise DeserializationError(
            "UpdateLaunchConfigurationRequest.source_server_id required"
        )
    if "name" in data:
        out["name"] = data["name"]
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
    if "postLaunchEnabled" in data:
        out["post_launch_enabled"] = data["postLaunchEnabled"]
    if "launchIntoInstanceProperties" in data:
        import aws_sdk_drs.types.launch_into_instance_properties

        out["launch_into_instance_properties"] = (
            aws_sdk_drs.types.launch_into_instance_properties.deserialize_json(
                data["launchIntoInstanceProperties"]
            )
        )
    return out
