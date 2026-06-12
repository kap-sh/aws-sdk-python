"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationConfigRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.organization_config_rule

OrganizationConfigRules: TypeAlias = list[
    "aws_sdk_config_service.types.organization_config_rule.OrganizationConfigRule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationConfigRules) -> list:
    import aws_sdk_config_service.types.organization_config_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.organization_config_rule.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OrganizationConfigRules:
    import aws_sdk_config_service.types.organization_config_rule

    out: OrganizationConfigRules = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.organization_config_rule.deserialize_aws_json_1_1(
                item
            )
        )
    return out
