"""Generated from Smithy shape ``com.amazonaws.devicefarm#UpdateDeviceInstanceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.amazon_resource_name
    import aws_sdk_device_farm.types.instance_labels


class UpdateDeviceInstanceRequest(TypedDict):
    arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the device instance.</p>"""
    profile_arn: NotRequired[
        "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the profile that you want to associate with the device instance.</p>"""
    labels: NotRequired["aws_sdk_device_farm.types.instance_labels.InstanceLabels"]
    """<p>An array of strings that you want to associate with the device instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDeviceInstanceRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "profile_arn" in value:
        out["profileArn"] = value["profile_arn"]
    if "labels" in value:
        import aws_sdk_device_farm.types.instance_labels

        out["labels"] = (
            aws_sdk_device_farm.types.instance_labels.serialize_aws_json_1_1(
                value["labels"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDeviceInstanceRequest:
    out: UpdateDeviceInstanceRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateDeviceInstanceRequest.arn required")
    if "profileArn" in data:
        out["profile_arn"] = data["profileArn"]
    if "labels" in data:
        import aws_sdk_device_farm.types.instance_labels

        out["labels"] = (
            aws_sdk_device_farm.types.instance_labels.deserialize_aws_json_1_1(
                data["labels"]
            )
        )
    return out
