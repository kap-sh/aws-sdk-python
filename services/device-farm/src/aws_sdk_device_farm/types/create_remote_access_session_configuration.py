"""Generated from Smithy shape ``com.amazonaws.devicefarm#CreateRemoteAccessSessionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.amazon_resource_names
    import aws_sdk_device_farm.types.auxiliary_app_arn_list
    import aws_sdk_device_farm.types.billing_method
    import aws_sdk_device_farm.types.device_proxy


class CreateRemoteAccessSessionConfiguration(TypedDict, closed=True):
    auxiliary_apps: NotRequired[
        "aws_sdk_device_farm.types.auxiliary_app_arn_list.AuxiliaryAppArnList"
    ]
    """<p>A list of upload ARNs for app packages to be installed onto your device. (Maximum 3)</p>"""
    billing_method: NotRequired[
        "aws_sdk_device_farm.types.billing_method.BillingMethod"
    ]
    """<p>The billing method for the remote access session.</p>"""
    vpce_configuration_arns: NotRequired[
        "aws_sdk_device_farm.types.amazon_resource_names.AmazonResourceNames"
    ]
    """<p>An array of ARNs included in the VPC endpoint configuration.</p>"""
    device_proxy: NotRequired["aws_sdk_device_farm.types.device_proxy.DeviceProxy"]
    """<p>The device proxy to be configured on the device for the remote access session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRemoteAccessSessionConfiguration) -> dict:
    out: dict = {}
    if "auxiliary_apps" in value:
        import aws_sdk_device_farm.types.auxiliary_app_arn_list

        out["auxiliaryApps"] = (
            aws_sdk_device_farm.types.auxiliary_app_arn_list.serialize_aws_json_1_1(
                value["auxiliary_apps"]
            )
        )
    if "billing_method" in value:
        import aws_sdk_device_farm.types.billing_method

        out["billingMethod"] = (
            aws_sdk_device_farm.types.billing_method.serialize_aws_json_1_1(
                value["billing_method"]
            )
        )
    if "vpce_configuration_arns" in value:
        import aws_sdk_device_farm.types.amazon_resource_names

        out["vpceConfigurationArns"] = (
            aws_sdk_device_farm.types.amazon_resource_names.serialize_aws_json_1_1(
                value["vpce_configuration_arns"]
            )
        )
    if "device_proxy" in value:
        import aws_sdk_device_farm.types.device_proxy

        out["deviceProxy"] = (
            aws_sdk_device_farm.types.device_proxy.serialize_aws_json_1_1(
                value["device_proxy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRemoteAccessSessionConfiguration:
    out: CreateRemoteAccessSessionConfiguration = {}  # type: ignore[typeddict-item]
    if "auxiliaryApps" in data:
        import aws_sdk_device_farm.types.auxiliary_app_arn_list

        out["auxiliary_apps"] = (
            aws_sdk_device_farm.types.auxiliary_app_arn_list.deserialize_aws_json_1_1(
                data["auxiliaryApps"]
            )
        )
    if "billingMethod" in data:
        import aws_sdk_device_farm.types.billing_method

        out["billing_method"] = (
            aws_sdk_device_farm.types.billing_method.deserialize_aws_json_1_1(
                data["billingMethod"]
            )
        )
    if "vpceConfigurationArns" in data:
        import aws_sdk_device_farm.types.amazon_resource_names

        out["vpce_configuration_arns"] = (
            aws_sdk_device_farm.types.amazon_resource_names.deserialize_aws_json_1_1(
                data["vpceConfigurationArns"]
            )
        )
    if "deviceProxy" in data:
        import aws_sdk_device_farm.types.device_proxy

        out["device_proxy"] = (
            aws_sdk_device_farm.types.device_proxy.deserialize_aws_json_1_1(
                data["deviceProxy"]
            )
        )
    return out
