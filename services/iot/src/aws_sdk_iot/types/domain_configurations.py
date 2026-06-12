"""Generated from Smithy shape ``com.amazonaws.iot#DomainConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.domain_configuration_summary

DomainConfigurations: TypeAlias = list[
    "aws_sdk_iot.types.domain_configuration_summary.DomainConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainConfigurations) -> list:
    import aws_sdk_iot.types.domain_configuration_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.domain_configuration_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DomainConfigurations:
    import aws_sdk_iot.types.domain_configuration_summary

    out: DomainConfigurations = []
    for item in data:
        out.append(
            aws_sdk_iot.types.domain_configuration_summary.deserialize_json(item)
        )
    return out
