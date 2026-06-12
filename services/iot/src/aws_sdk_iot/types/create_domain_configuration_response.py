"""Generated from Smithy shape ``com.amazonaws.iot#CreateDomainConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.domain_configuration_arn
    import aws_sdk_iot.types.domain_configuration_name


class CreateDomainConfigurationResponse(TypedDict):
    domain_configuration_name: NotRequired[
        "aws_sdk_iot.types.domain_configuration_name.DomainConfigurationName"
    ]
    """<p>The name of the domain configuration.</p>"""
    domain_configuration_arn: NotRequired[
        "aws_sdk_iot.types.domain_configuration_arn.DomainConfigurationArn"
    ]
    """<p>The ARN of the domain configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainConfigurationResponse) -> dict:
    out: dict = {}
    if "domain_configuration_name" in value:
        out["domainConfigurationName"] = value["domain_configuration_name"]
    if "domain_configuration_arn" in value:
        out["domainConfigurationArn"] = value["domain_configuration_arn"]
    return out


def deserialize_json(data: dict) -> CreateDomainConfigurationResponse:
    out: CreateDomainConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "domainConfigurationName" in data:
        out["domain_configuration_name"] = data["domainConfigurationName"]
    if "domainConfigurationArn" in data:
        out["domain_configuration_arn"] = data["domainConfigurationArn"]
    return out
