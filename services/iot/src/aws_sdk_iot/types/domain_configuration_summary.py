"""Generated from Smithy shape ``com.amazonaws.iot#DomainConfigurationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.domain_configuration_arn
    import aws_sdk_iot.types.reserved_domain_configuration_name
    import aws_sdk_iot.types.service_type


class DomainConfigurationSummary(TypedDict):
    domain_configuration_name: NotRequired[
        "aws_sdk_iot.types.reserved_domain_configuration_name.ReservedDomainConfigurationName"
    ]
    """<p>The name of the domain configuration. This value must be unique to a region.</p>"""
    domain_configuration_arn: NotRequired[
        "aws_sdk_iot.types.domain_configuration_arn.DomainConfigurationArn"
    ]
    """<p>The ARN of the domain configuration.</p>"""
    service_type: NotRequired["aws_sdk_iot.types.service_type.ServiceType"]
    """<p>The type of service delivered by the endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainConfigurationSummary) -> dict:
    out: dict = {}
    if "domain_configuration_name" in value:
        out["domainConfigurationName"] = value["domain_configuration_name"]
    if "domain_configuration_arn" in value:
        out["domainConfigurationArn"] = value["domain_configuration_arn"]
    if "service_type" in value:
        import aws_sdk_iot.types.service_type

        out["serviceType"] = aws_sdk_iot.types.service_type.serialize_json(
            value["service_type"]
        )
    return out


def deserialize_json(data: dict) -> DomainConfigurationSummary:
    out: DomainConfigurationSummary = {}  # type: ignore[typeddict-item]
    if "domainConfigurationName" in data:
        out["domain_configuration_name"] = data["domainConfigurationName"]
    if "domainConfigurationArn" in data:
        out["domain_configuration_arn"] = data["domainConfigurationArn"]
    if "serviceType" in data:
        import aws_sdk_iot.types.service_type

        out["service_type"] = aws_sdk_iot.types.service_type.deserialize_json(
            data["serviceType"]
        )
    return out
