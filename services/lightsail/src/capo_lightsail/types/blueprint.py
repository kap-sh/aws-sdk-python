"""Generated from Smithy shape ``com.amazonaws.lightsail#Blueprint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.app_category
    import capo_lightsail.types.blueprint_type
    import capo_lightsail.types.boolean
    import capo_lightsail.types.instance_platform
    import capo_lightsail.types.integer
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.string


class Blueprint(TypedDict, closed=True):
    blueprint_id: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The ID for the virtual private server image (<code>app_wordpress_x_x</code> or <code>app_lamp_x_x</code>).</p>"""
    name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The friendly name of the blueprint (<code>Amazon Linux</code>).</p>"""
    group: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The group name of the blueprint (<code>amazon-linux</code>).</p>"""
    type: NotRequired["capo_lightsail.types.blueprint_type.BlueprintType"]
    """<p>The type of the blueprint (<code>os</code> or <code>app</code>).</p>"""
    description: NotRequired["capo_lightsail.types.string.string"]
    """<p>The description of the blueprint.</p>"""
    is_active: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether the blueprint is active. Inactive blueprints are listed to support customers with existing instances but are not necessarily available for launch of new instances. Blueprints are marked inactive when they become outdated due to operating system updates or new application releases.</p>"""
    min_power: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>The minimum bundle power required to run this blueprint. For example, you need a bundle with a power value of 500 or more to create an instance that uses a blueprint with a minimum power value of 500. <code>0</code> indicates that the blueprint runs on all instance sizes. </p>"""
    version: NotRequired["capo_lightsail.types.string.string"]
    """<p>The version number of the operating system, application, or stack ( <code>2016.03.0</code>).</p>"""
    version_code: NotRequired["capo_lightsail.types.string.string"]
    """<p>The version code.</p>"""
    product_url: NotRequired["capo_lightsail.types.string.string"]
    """<p>The product URL to learn more about the image or blueprint.</p>"""
    license_url: NotRequired["capo_lightsail.types.string.string"]
    """<p>The end-user license agreement URL for the image or blueprint.</p>"""
    platform: NotRequired["capo_lightsail.types.instance_platform.InstancePlatform"]
    """<p>The operating system platform (either Linux/Unix-based or Windows Server-based) of the blueprint.</p>"""
    app_category: NotRequired["capo_lightsail.types.app_category.AppCategory"]
    """<p>Virtual computer blueprints that are supported by Lightsail for Research.</p> <important> <p>This parameter only applies to Lightsail for Research resources.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Blueprint) -> dict:
    out: dict = {}
    if "blueprint_id" in value:
        out["blueprintId"] = value["blueprint_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "group" in value:
        out["group"] = value["group"]
    if "type" in value:
        import capo_lightsail.types.blueprint_type

        out["type"] = capo_lightsail.types.blueprint_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "is_active" in value:
        out["isActive"] = value["is_active"]
    if "min_power" in value:
        out["minPower"] = value["min_power"]
    if "version" in value:
        out["version"] = value["version"]
    if "version_code" in value:
        out["versionCode"] = value["version_code"]
    if "product_url" in value:
        out["productUrl"] = value["product_url"]
    if "license_url" in value:
        out["licenseUrl"] = value["license_url"]
    if "platform" in value:
        import capo_lightsail.types.instance_platform

        out["platform"] = capo_lightsail.types.instance_platform.serialize_aws_json_1_1(
            value["platform"]
        )
    if "app_category" in value:
        import capo_lightsail.types.app_category

        out["appCategory"] = capo_lightsail.types.app_category.serialize_aws_json_1_1(
            value["app_category"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Blueprint:
    out: Blueprint = {}  # type: ignore[typeddict-item]
    if "blueprintId" in data:
        out["blueprint_id"] = data["blueprintId"]
    if "name" in data:
        out["name"] = data["name"]
    if "group" in data:
        out["group"] = data["group"]
    if "type" in data:
        import capo_lightsail.types.blueprint_type

        out["type"] = capo_lightsail.types.blueprint_type.deserialize_aws_json_1_1(
            data["type"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "isActive" in data:
        out["is_active"] = data["isActive"]
    if "minPower" in data:
        out["min_power"] = data["minPower"]
    if "version" in data:
        out["version"] = data["version"]
    if "versionCode" in data:
        out["version_code"] = data["versionCode"]
    if "productUrl" in data:
        out["product_url"] = data["productUrl"]
    if "licenseUrl" in data:
        out["license_url"] = data["licenseUrl"]
    if "platform" in data:
        import capo_lightsail.types.instance_platform

        out["platform"] = (
            capo_lightsail.types.instance_platform.deserialize_aws_json_1_1(
                data["platform"]
            )
        )
    if "appCategory" in data:
        import capo_lightsail.types.app_category

        out["app_category"] = (
            capo_lightsail.types.app_category.deserialize_aws_json_1_1(
                data["appCategory"]
            )
        )
    return out
