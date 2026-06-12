"""Generated from Smithy shape ``com.amazonaws.devicefarm#DevicePool``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.amazon_resource_name
    import aws_sdk_device_farm.types.device_pool_type
    import aws_sdk_device_farm.types.integer
    import aws_sdk_device_farm.types.message
    import aws_sdk_device_farm.types.name
    import aws_sdk_device_farm.types.rules


class DevicePool(TypedDict):
    arn: NotRequired[
        "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The device pool's ARN.</p>"""
    name: NotRequired["aws_sdk_device_farm.types.name.Name"]
    """<p>The device pool's name.</p>"""
    description: NotRequired["aws_sdk_device_farm.types.message.Message"]
    """<p>The device pool's description.</p>"""
    type: NotRequired["aws_sdk_device_farm.types.device_pool_type.DevicePoolType"]
    """<p>The device pool's type.</p> <p>Allowed values include:</p> <ul> <li> <p>CURATED: A device pool that is created and managed by AWS Device Farm.</p> </li> <li> <p>PRIVATE: A device pool that is created and managed by the device pool developer.</p> </li> </ul>"""
    rules: NotRequired["aws_sdk_device_farm.types.rules.Rules"]
    """<p>Information about the device pool's rules.</p>"""
    max_devices: NotRequired["aws_sdk_device_farm.types.integer.Integer"]
    """<p>The number of devices that Device Farm can add to your device pool. Device Farm adds devices that are available and meet the criteria that you assign for the <code>rules</code> parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter.</p> <p>By specifying the maximum number of devices, you can control the costs that you incur by running tests.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DevicePool) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "type" in value:
        import aws_sdk_device_farm.types.device_pool_type

        out["type"] = aws_sdk_device_farm.types.device_pool_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "rules" in value:
        import aws_sdk_device_farm.types.rules

        out["rules"] = aws_sdk_device_farm.types.rules.serialize_aws_json_1_1(
            value["rules"]
        )
    if "max_devices" in value:
        out["maxDevices"] = value["max_devices"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DevicePool:
    out: DevicePool = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "type" in data:
        import aws_sdk_device_farm.types.device_pool_type

        out["type"] = (
            aws_sdk_device_farm.types.device_pool_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    if "rules" in data:
        import aws_sdk_device_farm.types.rules

        out["rules"] = aws_sdk_device_farm.types.rules.deserialize_aws_json_1_1(
            data["rules"]
        )
    if "maxDevices" in data:
        out["max_devices"] = data["maxDevices"]
    return out
