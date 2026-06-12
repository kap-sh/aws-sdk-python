"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackConfigRuleNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.string_with_char_limit64

ConformancePackConfigRuleNames: TypeAlias = list[
    "aws_sdk_config_service.types.string_with_char_limit64.StringWithCharLimit64"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackConfigRuleNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ConformancePackConfigRuleNames:
    return list(data)
