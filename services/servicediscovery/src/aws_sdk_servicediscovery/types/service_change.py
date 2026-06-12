"""Generated from Smithy shape ``com.amazonaws.servicediscovery#ServiceChange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.dns_config_change
    import aws_sdk_servicediscovery.types.health_check_config
    import aws_sdk_servicediscovery.types.resource_description


class ServiceChange(TypedDict):
    description: NotRequired[
        "aws_sdk_servicediscovery.types.resource_description.ResourceDescription"
    ]
    """<p>A description for the service.</p>"""
    dns_config: NotRequired[
        "aws_sdk_servicediscovery.types.dns_config_change.DnsConfigChange"
    ]
    """<p>Information about the Route 53 DNS records that you want Cloud Map to create when you register an instance.</p>"""
    health_check_config: NotRequired[
        "aws_sdk_servicediscovery.types.health_check_config.HealthCheckConfig"
    ]
    """<p> <i>Public DNS and HTTP namespaces only.</i> Settings for an optional health check. If you specify settings for a health check, Cloud Map associates the health check with the records that you specify in <code>DnsConfig</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceChange) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "dns_config" in value:
        import aws_sdk_servicediscovery.types.dns_config_change

        out["DnsConfig"] = (
            aws_sdk_servicediscovery.types.dns_config_change.serialize_aws_json_1_1(
                value["dns_config"]
            )
        )
    if "health_check_config" in value:
        import aws_sdk_servicediscovery.types.health_check_config

        out["HealthCheckConfig"] = (
            aws_sdk_servicediscovery.types.health_check_config.serialize_aws_json_1_1(
                value["health_check_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceChange:
    out: ServiceChange = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DnsConfig" in data:
        import aws_sdk_servicediscovery.types.dns_config_change

        out["dns_config"] = (
            aws_sdk_servicediscovery.types.dns_config_change.deserialize_aws_json_1_1(
                data["DnsConfig"]
            )
        )
    if "HealthCheckConfig" in data:
        import aws_sdk_servicediscovery.types.health_check_config

        out["health_check_config"] = (
            aws_sdk_servicediscovery.types.health_check_config.deserialize_aws_json_1_1(
                data["HealthCheckConfig"]
            )
        )
    return out
