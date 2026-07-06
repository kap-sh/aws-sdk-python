"""Generated from Smithy shape ``com.amazonaws.devicefarm#DeviceInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.amazon_resource_name
    import aws_sdk_device_farm.types.instance_labels
    import aws_sdk_device_farm.types.instance_profile
    import aws_sdk_device_farm.types.instance_status
    import aws_sdk_device_farm.types.string


class DeviceInstance(TypedDict, closed=True):
    arn: NotRequired[
        "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the device instance.</p>"""
    device_arn: NotRequired[
        "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the device.</p>"""
    labels: NotRequired["aws_sdk_device_farm.types.instance_labels.InstanceLabels"]
    """<p>An array of strings that describe the device instance.</p>"""
    status: NotRequired["aws_sdk_device_farm.types.instance_status.InstanceStatus"]
    """<p>The status of the device instance. Valid values are listed here.</p>"""
    udid: NotRequired["aws_sdk_device_farm.types.string.String"]
    """<p>Unique device identifier for the device instance.</p>"""
    instance_profile: NotRequired[
        "aws_sdk_device_farm.types.instance_profile.InstanceProfile"
    ]
    """<p>A object that contains information about the instance profile.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceInstance) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "device_arn" in value:
        out["deviceArn"] = value["device_arn"]
    if "labels" in value:
        import aws_sdk_device_farm.types.instance_labels

        out["labels"] = (
            aws_sdk_device_farm.types.instance_labels.serialize_aws_json_1_1(
                value["labels"]
            )
        )
    if "status" in value:
        import aws_sdk_device_farm.types.instance_status

        out["status"] = (
            aws_sdk_device_farm.types.instance_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "udid" in value:
        out["udid"] = value["udid"]
    if "instance_profile" in value:
        import aws_sdk_device_farm.types.instance_profile

        out["instanceProfile"] = (
            aws_sdk_device_farm.types.instance_profile.serialize_aws_json_1_1(
                value["instance_profile"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeviceInstance:
    out: DeviceInstance = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "deviceArn" in data:
        out["device_arn"] = data["deviceArn"]
    if "labels" in data:
        import aws_sdk_device_farm.types.instance_labels

        out["labels"] = (
            aws_sdk_device_farm.types.instance_labels.deserialize_aws_json_1_1(
                data["labels"]
            )
        )
    if "status" in data:
        import aws_sdk_device_farm.types.instance_status

        out["status"] = (
            aws_sdk_device_farm.types.instance_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "udid" in data:
        out["udid"] = data["udid"]
    if "instanceProfile" in data:
        import aws_sdk_device_farm.types.instance_profile

        out["instance_profile"] = (
            aws_sdk_device_farm.types.instance_profile.deserialize_aws_json_1_1(
                data["instanceProfile"]
            )
        )
    return out
