"""Generated from Smithy shape ``com.amazonaws.devopsagent#DescribePrivateConnectionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_devops_agent.types.failure_message
    import aws_sdk_devops_agent.types.ip_address_or_dns_name
    import aws_sdk_devops_agent.types.private_connection_name
    import aws_sdk_devops_agent.types.private_connection_status
    import aws_sdk_devops_agent.types.private_connection_type
    import aws_sdk_devops_agent.types.resource_config_dns_resolution
    import aws_sdk_devops_agent.types.resource_configuration_arn
    import aws_sdk_devops_agent.types.resource_gateway_arn
    import aws_sdk_devops_agent.types.tags
    import aws_sdk_devops_agent.types.vpc_id


class DescribePrivateConnectionOutput(TypedDict, closed=True):
    name: "aws_sdk_devops_agent.types.private_connection_name.PrivateConnectionName"
    """<p>The name of the Private Connection.</p>"""
    type: "aws_sdk_devops_agent.types.private_connection_type.PrivateConnectionType"
    """<p>The type of the Private Connection.</p>"""
    resource_gateway_id: NotRequired[
        "aws_sdk_devops_agent.types.resource_gateway_arn.ResourceGatewayArn"
    ]
    """<p>The service-managed Resource Gateway ARN. Only present for service-managed Private Connections.</p>"""
    host_address: NotRequired[
        "aws_sdk_devops_agent.types.ip_address_or_dns_name.IpAddressOrDnsName"
    ]
    """<p>IP address or DNS name of the target resource. Only present for service-managed Private Connections.</p>"""
    vpc_id: NotRequired["aws_sdk_devops_agent.types.vpc_id.VpcId"]
    """<p>VPC identifier of the service-managed Resource Gateway. Only present for service-managed Private Connections.</p>"""
    resource_configuration_id: NotRequired[
        "aws_sdk_devops_agent.types.resource_configuration_arn.ResourceConfigurationArn"
    ]
    """<p>The Resource Configuration ARN. Only present for self-managed Private Connections.</p>"""
    status: (
        "aws_sdk_devops_agent.types.private_connection_status.PrivateConnectionStatus"
    )
    """<p>The status of the Private Connection.</p>"""
    certificate_expiry_time: NotRequired["datetime.datetime"]
    """<p>The expiry time of the certificate associated with the Private Connection. Only present when a certificate is associated.</p>"""
    dns_resolution: NotRequired[
        "aws_sdk_devops_agent.types.resource_config_dns_resolution.ResourceConfigDnsResolution"
    ]
    """<p>DNS resolution mode for the Private Connection's resource gateway.</p>"""
    failure_message: NotRequired[
        "aws_sdk_devops_agent.types.failure_message.FailureMessage"
    ]
    """<p>Message describing the reason for a failed Private Connection, if applicable.</p>"""
    tags: NotRequired["aws_sdk_devops_agent.types.tags.Tags"]
    """<p>Tags associated with the Private Connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePrivateConnectionOutput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_devops_agent.types.private_connection_type

    out["type"] = aws_sdk_devops_agent.types.private_connection_type.serialize_json(
        value["type"]
    )
    if "resource_gateway_id" in value:
        out["resourceGatewayId"] = value["resource_gateway_id"]
    if "host_address" in value:
        out["hostAddress"] = value["host_address"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "resource_configuration_id" in value:
        out["resourceConfigurationId"] = value["resource_configuration_id"]
    import aws_sdk_devops_agent.types.private_connection_status

    out["status"] = aws_sdk_devops_agent.types.private_connection_status.serialize_json(
        value["status"]
    )
    if "certificate_expiry_time" in value:
        import aws_sdk_devops_agent.types._prelude.timestamp

        out["certificateExpiryTime"] = (
            aws_sdk_devops_agent.types._prelude.timestamp.serialize_json(
                value["certificate_expiry_time"]
            )
        )
    if "dns_resolution" in value:
        import aws_sdk_devops_agent.types.resource_config_dns_resolution

        out["dnsResolution"] = (
            aws_sdk_devops_agent.types.resource_config_dns_resolution.serialize_json(
                value["dns_resolution"]
            )
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    if "tags" in value:
        import aws_sdk_devops_agent.types.tags

        out["tags"] = aws_sdk_devops_agent.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DescribePrivateConnectionOutput:
    out: DescribePrivateConnectionOutput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DescribePrivateConnectionOutput.name required")
    if "type" in data:
        import aws_sdk_devops_agent.types.private_connection_type

        out["type"] = (
            aws_sdk_devops_agent.types.private_connection_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("DescribePrivateConnectionOutput.type required")
    if "resourceGatewayId" in data:
        out["resource_gateway_id"] = data["resourceGatewayId"]
    if "hostAddress" in data:
        out["host_address"] = data["hostAddress"]
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    if "resourceConfigurationId" in data:
        out["resource_configuration_id"] = data["resourceConfigurationId"]
    if "status" in data:
        import aws_sdk_devops_agent.types.private_connection_status

        out["status"] = (
            aws_sdk_devops_agent.types.private_connection_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DescribePrivateConnectionOutput.status required")
    if "certificateExpiryTime" in data:
        import aws_sdk_devops_agent.types._prelude.timestamp

        out["certificate_expiry_time"] = (
            aws_sdk_devops_agent.types._prelude.timestamp.deserialize_json(
                data["certificateExpiryTime"]
            )
        )
    if "dnsResolution" in data:
        import aws_sdk_devops_agent.types.resource_config_dns_resolution

        out["dns_resolution"] = (
            aws_sdk_devops_agent.types.resource_config_dns_resolution.deserialize_json(
                data["dnsResolution"]
            )
        )
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
    if "tags" in data:
        import aws_sdk_devops_agent.types.tags

        out["tags"] = aws_sdk_devops_agent.types.tags.deserialize_json(data["tags"])
    return out
