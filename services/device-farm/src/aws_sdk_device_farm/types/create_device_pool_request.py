"""Generated from Smithy shape ``com.amazonaws.devicefarm#CreateDevicePoolRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.amazon_resource_name
    import aws_sdk_device_farm.types.integer
    import aws_sdk_device_farm.types.message
    import aws_sdk_device_farm.types.name
    import aws_sdk_device_farm.types.rules


class CreateDevicePoolRequest(TypedDict):
    project_arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the project for the device pool.</p>"""
    name: "aws_sdk_device_farm.types.name.Name"
    """<p>The device pool's name.</p>"""
    description: NotRequired["aws_sdk_device_farm.types.message.Message"]
    """<p>The device pool's description.</p>"""
    rules: "aws_sdk_device_farm.types.rules.Rules"
    """<p>The device pool's rules.</p>"""
    max_devices: NotRequired["aws_sdk_device_farm.types.integer.Integer"]
    """<p>The number of devices that Device Farm can add to your device pool. Device Farm adds devices that are available and meet the criteria that you assign for the <code>rules</code> parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter.</p> <p>By specifying the maximum number of devices, you can control the costs that you incur by running tests.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDevicePoolRequest) -> dict:
    out: dict = {}
    out["projectArn"] = value["project_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_device_farm.types.rules

    out["rules"] = aws_sdk_device_farm.types.rules.serialize_aws_json_1_1(
        value["rules"]
    )
    if "max_devices" in value:
        out["maxDevices"] = value["max_devices"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDevicePoolRequest:
    out: CreateDevicePoolRequest = {}  # type: ignore[typeddict-item]
    if "projectArn" in data:
        out["project_arn"] = data["projectArn"]
    else:
        raise DeserializationError("CreateDevicePoolRequest.project_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDevicePoolRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "rules" in data:
        import aws_sdk_device_farm.types.rules

        out["rules"] = aws_sdk_device_farm.types.rules.deserialize_aws_json_1_1(
            data["rules"]
        )
    else:
        raise DeserializationError("CreateDevicePoolRequest.rules required")
    if "maxDevices" in data:
        out["max_devices"] = data["maxDevices"]
    return out
