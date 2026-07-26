"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationConfigRuleNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.string_with_char_limit64

OrganizationConfigRuleNames: TypeAlias = list[
    "capo_config_service.types.string_with_char_limit64.StringWithCharLimit64"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationConfigRuleNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OrganizationConfigRuleNames:
    return list(data)
