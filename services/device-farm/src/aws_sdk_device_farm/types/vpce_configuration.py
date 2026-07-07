"""Generated from Smithy shape ``com.amazonaws.devicefarm#VPCEConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.amazon_resource_name
    import aws_sdk_device_farm.types.service_dns_name
    import aws_sdk_device_farm.types.vpce_configuration_description
    import aws_sdk_device_farm.types.vpce_configuration_name
    import aws_sdk_device_farm.types.vpce_service_name


class VPCEConfiguration(TypedDict, closed=True):
    arn: NotRequired[
        "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the VPC endpoint configuration.</p>"""
    vpce_configuration_name: NotRequired[
        "aws_sdk_device_farm.types.vpce_configuration_name.VPCEConfigurationName"
    ]
    """<p>The friendly name you give to your VPC endpoint configuration to manage your configurations more easily.</p>"""
    vpce_service_name: NotRequired[
        "aws_sdk_device_farm.types.vpce_service_name.VPCEServiceName"
    ]
    """<p>The name of the VPC endpoint service running in your AWS account that you want Device Farm to test.</p>"""
    service_dns_name: NotRequired[
        "aws_sdk_device_farm.types.service_dns_name.ServiceDnsName"
    ]
    """<p>The DNS name that maps to the private IP address of the service you want to access.</p>"""
    vpce_configuration_description: NotRequired[
        "aws_sdk_device_farm.types.vpce_configuration_description.VPCEConfigurationDescription"
    ]
    """<p>An optional description that provides details about your VPC endpoint configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VPCEConfiguration) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "vpce_configuration_name" in value:
        out["vpceConfigurationName"] = value["vpce_configuration_name"]
    if "vpce_service_name" in value:
        out["vpceServiceName"] = value["vpce_service_name"]
    if "service_dns_name" in value:
        out["serviceDnsName"] = value["service_dns_name"]
    if "vpce_configuration_description" in value:
        out["vpceConfigurationDescription"] = value["vpce_configuration_description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VPCEConfiguration:
    out: VPCEConfiguration = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "vpceConfigurationName" in data:
        out["vpce_configuration_name"] = data["vpceConfigurationName"]
    if "vpceServiceName" in data:
        out["vpce_service_name"] = data["vpceServiceName"]
    if "serviceDnsName" in data:
        out["service_dns_name"] = data["serviceDnsName"]
    if "vpceConfigurationDescription" in data:
        out["vpce_configuration_description"] = data["vpceConfigurationDescription"]
    return out
