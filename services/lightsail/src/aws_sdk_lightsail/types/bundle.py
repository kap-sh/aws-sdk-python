"""Generated from Smithy shape ``com.amazonaws.lightsail#Bundle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.app_category_list
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.float
    import aws_sdk_lightsail.types.instance_platform_list
    import aws_sdk_lightsail.types.integer
    import aws_sdk_lightsail.types.non_empty_string
    import aws_sdk_lightsail.types.string


class Bundle(TypedDict, closed=True):
    price: NotRequired["aws_sdk_lightsail.types.float.float"]
    """<p>The price in US dollars (<code>5.0</code>) of the bundle.</p>"""
    cpu_count: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>The number of vCPUs included in the bundle (<code>2</code>).</p>"""
    disk_size_in_gb: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>The size of the SSD (<code>30</code>).</p>"""
    bundle_id: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The bundle ID (<code>micro_x_x</code>).</p>"""
    instance_type: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The instance type (<code>micro</code>).</p>"""
    is_active: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether the bundle is active.</p>"""
    name: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>A friendly name for the bundle (<code>Micro</code>).</p>"""
    power: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>A numeric value that represents the power of the bundle (<code>500</code>). You can use the bundle's power value in conjunction with a blueprint's minimum power value to determine whether the blueprint will run on the bundle. For example, you need a bundle with a power value of 500 or more to create an instance that uses a blueprint with a minimum power value of 500.</p>"""
    ram_size_in_gb: NotRequired["aws_sdk_lightsail.types.float.float"]
    """<p>The amount of RAM in GB (<code>2.0</code>).</p>"""
    transfer_per_month_in_gb: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>The data transfer rate per month in GB (<code>2000</code>).</p>"""
    supported_platforms: NotRequired[
        "aws_sdk_lightsail.types.instance_platform_list.InstancePlatformList"
    ]
    """<p>The operating system platform (Linux/Unix-based or Windows Server-based) that the bundle supports. You can only launch a <code>WINDOWS</code> bundle on a blueprint that supports the <code>WINDOWS</code> platform. <code>LINUX_UNIX</code> blueprints require a <code>LINUX_UNIX</code> bundle.</p>"""
    supported_app_categories: NotRequired[
        "aws_sdk_lightsail.types.app_category_list.AppCategoryList"
    ]
    """<p>Virtual computer blueprints that are supported by a Lightsail for Research bundle.</p> <important> <p>This parameter only applies to Lightsail for Research resources.</p> </important>"""
    public_ipv4_address_count: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>An integer that indicates the public ipv4 address count included in the bundle, the value is either 0 or 1.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Bundle) -> dict:
    out: dict = {}
    if "price" in value:
        out["price"] = value["price"]
    if "cpu_count" in value:
        out["cpuCount"] = value["cpu_count"]
    if "disk_size_in_gb" in value:
        out["diskSizeInGb"] = value["disk_size_in_gb"]
    if "bundle_id" in value:
        out["bundleId"] = value["bundle_id"]
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "is_active" in value:
        out["isActive"] = value["is_active"]
    if "name" in value:
        out["name"] = value["name"]
    if "power" in value:
        out["power"] = value["power"]
    if "ram_size_in_gb" in value:
        out["ramSizeInGb"] = value["ram_size_in_gb"]
    if "transfer_per_month_in_gb" in value:
        out["transferPerMonthInGb"] = value["transfer_per_month_in_gb"]
    if "supported_platforms" in value:
        import aws_sdk_lightsail.types.instance_platform_list

        out["supportedPlatforms"] = (
            aws_sdk_lightsail.types.instance_platform_list.serialize_aws_json_1_1(
                value["supported_platforms"]
            )
        )
    if "supported_app_categories" in value:
        import aws_sdk_lightsail.types.app_category_list

        out["supportedAppCategories"] = (
            aws_sdk_lightsail.types.app_category_list.serialize_aws_json_1_1(
                value["supported_app_categories"]
            )
        )
    if "public_ipv4_address_count" in value:
        out["publicIpv4AddressCount"] = value["public_ipv4_address_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Bundle:
    out: Bundle = {}  # type: ignore[typeddict-item]
    if "price" in data:
        out["price"] = data["price"]
    if "cpuCount" in data:
        out["cpu_count"] = data["cpuCount"]
    if "diskSizeInGb" in data:
        out["disk_size_in_gb"] = data["diskSizeInGb"]
    if "bundleId" in data:
        out["bundle_id"] = data["bundleId"]
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    if "isActive" in data:
        out["is_active"] = data["isActive"]
    if "name" in data:
        out["name"] = data["name"]
    if "power" in data:
        out["power"] = data["power"]
    if "ramSizeInGb" in data:
        out["ram_size_in_gb"] = data["ramSizeInGb"]
    if "transferPerMonthInGb" in data:
        out["transfer_per_month_in_gb"] = data["transferPerMonthInGb"]
    if "supportedPlatforms" in data:
        import aws_sdk_lightsail.types.instance_platform_list

        out["supported_platforms"] = (
            aws_sdk_lightsail.types.instance_platform_list.deserialize_aws_json_1_1(
                data["supportedPlatforms"]
            )
        )
    if "supportedAppCategories" in data:
        import aws_sdk_lightsail.types.app_category_list

        out["supported_app_categories"] = (
            aws_sdk_lightsail.types.app_category_list.deserialize_aws_json_1_1(
                data["supportedAppCategories"]
            )
        )
    if "publicIpv4AddressCount" in data:
        out["public_ipv4_address_count"] = data["publicIpv4AddressCount"]
    return out
