"""Generated from Smithy shape ``com.amazonaws.iot#UpdateDomainConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.domain_configuration_arn
    import capo_iot.types.reserved_domain_configuration_name


class UpdateDomainConfigurationResponse(TypedDict, closed=True):
    domain_configuration_name: NotRequired[
        "capo_iot.types.reserved_domain_configuration_name.ReservedDomainConfigurationName"
    ]
    """<p>The name of the domain configuration that was updated.</p>"""
    domain_configuration_arn: NotRequired[
        "capo_iot.types.domain_configuration_arn.DomainConfigurationArn"
    ]
    """<p>The ARN of the domain configuration that was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDomainConfigurationResponse) -> dict:
    out: dict = {}
    if "domain_configuration_name" in value:
        out["domainConfigurationName"] = value["domain_configuration_name"]
    if "domain_configuration_arn" in value:
        out["domainConfigurationArn"] = value["domain_configuration_arn"]
    return out


def deserialize_json(data: dict) -> UpdateDomainConfigurationResponse:
    out: UpdateDomainConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "domainConfigurationName" in data:
        out["domain_configuration_name"] = data["domainConfigurationName"]
    if "domainConfigurationArn" in data:
        out["domain_configuration_arn"] = data["domainConfigurationArn"]
    return out
