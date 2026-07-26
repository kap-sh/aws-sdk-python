"""Generated from Smithy shape ``com.amazonaws.configservice#RemediationConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.remediation_configuration

RemediationConfigurations: TypeAlias = list[
    "capo_config_service.types.remediation_configuration.RemediationConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemediationConfigurations) -> list:
    import capo_config_service.types.remediation_configuration

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.remediation_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RemediationConfigurations:
    import capo_config_service.types.remediation_configuration

    out: RemediationConfigurations = []
    for item in data:
        out.append(
            capo_config_service.types.remediation_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
