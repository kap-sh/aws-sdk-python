"""Generated from Smithy shape ``com.amazonaws.devicefarm#InstanceProfile``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.amazon_resource_name
    import aws_sdk_device_farm.types.boolean
    import aws_sdk_device_farm.types.message
    import aws_sdk_device_farm.types.name
    import aws_sdk_device_farm.types.package_ids


class InstanceProfile(TypedDict):
    arn: NotRequired[
        "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the instance profile.</p>"""
    package_cleanup: NotRequired["aws_sdk_device_farm.types.boolean.Boolean"]
    """<p>When set to <code>true</code>, Device Farm removes app packages after a test run. The default value is <code>false</code> for private devices.</p>"""
    exclude_app_packages_from_cleanup: NotRequired[
        "aws_sdk_device_farm.types.package_ids.PackageIds"
    ]
    """<p>An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes.</p> <p>The list of packages is considered only if you set <code>packageCleanup</code> to <code>true</code>.</p>"""
    reboot_after_use: NotRequired["aws_sdk_device_farm.types.boolean.Boolean"]
    """<p>When set to <code>true</code>, Device Farm reboots the instance after a test run. The default value is <code>true</code>.</p>"""
    name: NotRequired["aws_sdk_device_farm.types.name.Name"]
    """<p>The name of the instance profile.</p>"""
    description: NotRequired["aws_sdk_device_farm.types.message.Message"]
    """<p>The description of the instance profile.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceProfile) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "package_cleanup" in value:
        out["packageCleanup"] = value["package_cleanup"]
    if "exclude_app_packages_from_cleanup" in value:
        import aws_sdk_device_farm.types.package_ids

        out["excludeAppPackagesFromCleanup"] = (
            aws_sdk_device_farm.types.package_ids.serialize_aws_json_1_1(
                value["exclude_app_packages_from_cleanup"]
            )
        )
    if "reboot_after_use" in value:
        out["rebootAfterUse"] = value["reboot_after_use"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceProfile:
    out: InstanceProfile = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "packageCleanup" in data:
        out["package_cleanup"] = data["packageCleanup"]
    if "excludeAppPackagesFromCleanup" in data:
        import aws_sdk_device_farm.types.package_ids

        out["exclude_app_packages_from_cleanup"] = (
            aws_sdk_device_farm.types.package_ids.deserialize_aws_json_1_1(
                data["excludeAppPackagesFromCleanup"]
            )
        )
    if "rebootAfterUse" in data:
        out["reboot_after_use"] = data["rebootAfterUse"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    return out
