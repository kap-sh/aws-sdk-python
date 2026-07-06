"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServicePower``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.float
    import aws_sdk_lightsail.types.string


class ContainerServicePower(TypedDict, closed=True):
    power_id: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The ID of the power (<code>nano-1</code>).</p>"""
    price: NotRequired["aws_sdk_lightsail.types.float.float"]
    """<p>The monthly price of the power in USD.</p>"""
    cpu_count: NotRequired["aws_sdk_lightsail.types.float.float"]
    """<p>The number of vCPUs included in the power.</p>"""
    ram_size_in_gb: NotRequired["aws_sdk_lightsail.types.float.float"]
    """<p>The amount of RAM (in GB) of the power.</p>"""
    name: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The friendly name of the power (<code>nano</code>).</p>"""
    is_active: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether the power is active and can be specified for container services.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerServicePower) -> dict:
    out: dict = {}
    if "power_id" in value:
        out["powerId"] = value["power_id"]
    if "price" in value:
        out["price"] = value["price"]
    if "cpu_count" in value:
        out["cpuCount"] = value["cpu_count"]
    if "ram_size_in_gb" in value:
        out["ramSizeInGb"] = value["ram_size_in_gb"]
    if "name" in value:
        out["name"] = value["name"]
    if "is_active" in value:
        out["isActive"] = value["is_active"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerServicePower:
    out: ContainerServicePower = {}  # type: ignore[typeddict-item]
    if "powerId" in data:
        out["power_id"] = data["powerId"]
    if "price" in data:
        out["price"] = data["price"]
    if "cpuCount" in data:
        out["cpu_count"] = data["cpuCount"]
    if "ramSizeInGb" in data:
        out["ram_size_in_gb"] = data["ramSizeInGb"]
    if "name" in data:
        out["name"] = data["name"]
    if "isActive" in data:
        out["is_active"] = data["isActive"]
    return out
